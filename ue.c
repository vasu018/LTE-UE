#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <sys/types.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <unistd.h>
#include <pthread.h>
#include "ue.h"
#include <time.h>
#include <errno.h>
#include <sys/time.h>
#include <signal.h>

#define DEF_CLOCK 0
#define DEF_GETTIMEOFDAY 1
#define DEF_GET_ONE_SEC_CONN

int rrval = 1;
double total_time = 0;
double serv_time = 0;
int serial_num=1;
system_stats_t global_stats;
int first_time_flag = 1;
int break_flag = 0;
double              rand_total_time;
uint32_t            rand_thread, rand_serial;


void
accumulate_stat(system_stats_t *dest_stats, system_stats_t *src_stats)
{
    dest_stats->attach_attempt         += src_stats->attach_attempt;
    dest_stats->attach_nas_req_recv    += src_stats->attach_nas_req_recv;
    dest_stats->attach_nas_resp_sent   += src_stats->attach_nas_resp_sent;
    dest_stats->attach_auth_req_recv   += src_stats->attach_auth_req_recv;
    dest_stats->attach_auth_resp_sent  += src_stats->attach_auth_resp_sent;
    dest_stats->attach_accept_recv     += src_stats->attach_accept_recv;
    dest_stats->attach_accept_complete_sent    += src_stats->attach_accept_complete_sent;
    dest_stats->attach_fail            += src_stats->attach_fail;
    
#if 0
    /*
     * We want to flush src stats since they have been accounted for
     */
    memset(src_stats, 0, sizeof(system_stats_t));
#endif

    return;
}

int
increment_system_stat(system_stats_t *stats, int stat)
{
    switch (stat) {
    case STAT_ATTACH_ATTEMPT:
        stats->attach_attempt++;
        break;
    case STAT_ATTACH_NAS_REQ_RECV:
        stats->attach_nas_req_recv++;
        break;
    case STAT_ATTACH_NAS_RESP_SENT:
        stats->attach_nas_resp_sent++;
        break;
    case STAT_ATTACH_AUTH_REQ_RECV:
        stats->attach_auth_req_recv++;
        break;
    case STAT_ATTACH_AUTH_RESP_SENT:
        stats->attach_auth_resp_sent++;
        break;
    case STAT_ATTACH_ACCEPT_RECV:
        stats->attach_accept_recv++;
        break;
    case STAT_ATTACH_ACCEPT_COMPLETE_SENT:
        stats->attach_accept_complete_sent++;
        break;
    case STAT_ATTACH_FAIL:
        stats->attach_fail++;
        break;
    default:
        break;
    }
    return 1;
}
void
show_system_thread_stats(thread_state_t *thread_state, int num_threads)
{
    int i;

    printf("\n\n**************** System Stats *******************\n");
    printf("Thread_ID\t#SuccessConn\tAtch_fail\tAtch_attempt\tauth_recv\tnas_recv\n\n");

    for (i = 0; i< num_threads; i++) {
        printf("%d\t\t%lu\t\t%lu\t\t%lu\t\t%lu\t\t%lu\n",
               thread_state[i].thread_num,
               thread_state[i].thread_stats.attach_accept_complete_sent,
               thread_state[i].thread_stats.attach_fail,
               thread_state[i].thread_stats.attach_attempt,
               thread_state[i].thread_stats.attach_auth_req_recv,
               thread_state[i].thread_stats.attach_nas_req_recv);
    }

}
void
show_time_thread_stats(thread_state_t *thread_state, int num_threads)
{
    int i;
    printf("\n\n**************** Time Stats *******************\n");
    printf("Thread_ID\t#SuccessConn\tAtch_Total\tInitiate->Auth\tAuth->NAS\tNAS->Accept\n\n");

    for (i = 0; i< num_threads; i++) {
        printf("%d\t\t%lu\t\t%f\t%f\t%f\t%f\n",
               thread_state[i].thread_num,
               thread_state[i].thread_stats.attach_accept_complete_sent,
               thread_state[i].thread_time_stats.attach_total / 
               thread_state[i].thread_stats.attach_accept_complete_sent,

               thread_state[i].thread_time_stats.attach_initiate_to_auth_recv /
               thread_state[i].thread_stats.attach_accept_complete_sent,

               thread_state[i].thread_time_stats.attach_auth_send_to_nas_recv /
               thread_state[i].thread_stats.attach_accept_complete_sent,

               thread_state[i].thread_time_stats.attach_nas_recv_to_accept /
               thread_state[i].thread_stats.attach_accept_complete_sent);
    }

}

void
show_exit_counter_stats(system_stats_t *stats)
{
    printf("\n\n**************** Exit counters *******************\n");
    printf("\t\tRequest\t\tSuccessful\t\tFail\t\tTime\n");
    printf("Attach\t\t%lu\t\t%lu\t\t\t%lu\t\t%f\n",
           stats->attach_attempt,
           stats->attach_accept_complete_sent,
           stats->attach_fail,
           total_time);
    printf("Service\t\t%lu\t\t%lu\t\t\t%lu\t\t%f\n",
           stats->service_attempt,
           stats->service_successful,
           stats->service_attempt - stats->service_successful,
           total_time);
}

void
show_time_global_stats()
{
    printf("\n\n**************** Time Global Stats *******************\n");
    printf("Thread ID %d Serial ID %d ran for %lf ms\n",
           rand_thread, rand_serial, rand_total_time);
}

void
show_system_global_stats()
{
    printf("\n\n**************** System Global Stats *******************\n");
    printf("ATTACH_ATTEMPT \t\t\t= %lu\n"
    "ATTACH_AUTH_REQ_RECV \t\t= %lu\n"
    "ATTACH_AUTH_RESP_SENT \t\t= %lu\n"
    "ATTACH_NAS_REQ_RECV \t\t= %lu\n"
    "ATTACH_NAS_RESP_SENT \t\t= %lu\n"
    "ATTACH_ACCEPT_RECV \t\t= %lu\n"
    "ATTACH_ACCEPT_COMPLETE_SENT \t= %lu\n",
    global_stats.attach_attempt,
    global_stats.attach_auth_req_recv,
    global_stats.attach_auth_resp_sent,
    global_stats.attach_nas_req_recv,
    global_stats.attach_nas_resp_sent,
    global_stats.attach_accept_recv,
    global_stats.attach_accept_complete_sent);
}

void diep(char *s)
{
  perror(s);
}

void sig_handler(int signo)
{
    if (signo == SIGINT) {
        printf("Received SIGINT!!!\n");
        show_system_global_stats();
        show_exit_counter_stats(&global_stats);
        break_flag = 1;
#if 0
        show_time_thread_stats(thread_state, num_threads);
        show_system_thread_stats(thread_state, num_threads);
#endif
    }
}

int hex_to_num(char *hex, int8_t *num_array)
{
    int len, i=0, num, j=0;
    char temp[2];

    len = strlen(hex);

    while(i+1 < len) {
        temp[0] = hex[i];
        temp[1] = hex[i+1];
        num = (int8_t)strtol(temp, NULL, 16);
        i += 2;
        num_array[j++] = num;
    }
    return 0;

}

int
put_enb_ue_s1ap_id(uint8_t* pkt_enb_id_ptr, uint32_t enb_id)
{
    uint8_t *start = pkt_enb_id_ptr; 
    
    memcpy(start, &enb_id, sizeof(uint32_t));
    return 0;
}

void
print_imsi(uint8_t* imsi_p)
{
    int i;
    uint64_t ans=0;
    uint8_t *start = imsi_p+4;

    for (i=0; i<4; i++) {
        ans = ans * 10;
        ans += (*start & 0xf0) >> 4;
        ans = ans * 10;
        ans += (*start & 0x0f);
        start += 1;
    }

    printf("Imsi value = %lu\n",ans);
}

int
increase_imsi_serial(uint8_t* imsi_p, int increment_val)
{
    int i;
    uint64_t ans=0;
    uint8_t *start = imsi_p+6;
    uint32_t digit;

    for (i=0; i<2; i++) {
        ans = ans * 10;
        ans += (*start & 0xf0) >> 4;
        ans = ans * 10;
        ans += (*start & 0x0f);
        start += 1;
    }

#if 0
    printf("increment serial imsi by = %d\n",increment_val);
#endif

    ans += increment_val;

#if 0
    printf("Serial imsi ans= %lu\n",ans);
#endif
    start = imsi_p+7;
    for (i=2; i>0; i--) {
        digit = ans % 10;
        ans = ans/10;
        *start = digit & 0x0f;

        digit = ans % 10;
        ans = ans/10;
        *start = *start | ((digit & 0x0f) << 4);
        start -= 1;
    }
    return 0;
}

int
increase_imsi_thread(uint8_t* imsi_p, int increment_val)
{
    int i;
    uint64_t ans=0;
    uint8_t *start = imsi_p+4;
    uint32_t digit;

    for (i=0; i<2; i++) {
        ans = ans * 10;
        ans += (*start & 0xf0) >> 4;
        ans = ans * 10;
        ans += (*start & 0x0f);
        start += 1;
    }

#if 0
    printf("increment thread imsi by = %d\n",increment_val);
#endif

    ans += increment_val;

#if 0
    printf("Thread imsi ans= %lu\n",ans);
#endif
    start = imsi_p+5;
    for (i=2; i>0; i--) {
        digit = ans % 10;
        ans = ans/10;
        *start = digit & 0x0f;

        digit = ans % 10;
        ans = ans/10;
        *start = *start | ((digit & 0x0f) << 4);
        start -= 1;
    }
    return 0;
}


int
service_req(void *arg)
{
    uint32_t            slen=sizeof(struct sockaddr_in);
    char                buf_array[BUFLEN], *buf_start, *buf;
    thread_state_t      *thread_state = (thread_state_t*)arg;
    int                 s = thread_state->socket;
    uint8_t             attach_code = 0x4d;
    clock_t             start, end;
    double              cpu_time_used=0;
    pkt_identifier_t    pkt_identifier;
    int                 err=0;
    uint32_t            enb_ue_s1ap_id = 0;

    enb_ue_s1ap_id = (thread_state->thread_num + thread_state->thread_seed)* 10000 +
                    thread_state->serial_seed;
    
    char payload[] = "000c005c0000050008000480646dbe001a00323107417108298039100000111102802000200201d011271a8080211001000010810600000000830600000000000d00000a00004300060002f8390001006440080002f83900e000000086400130\0";

    pkt_identifier.slice_id = 1;
    pkt_identifier.msg_type = PKT_TYPE_SERVICE;
    /* Keep the start pointer to use for sending
     */
    buf = buf_array;
    buf_start = buf;
    memcpy(buf_start, &pkt_identifier, sizeof(pkt_identifier_t));
    buf = buf_start + sizeof(pkt_identifier_t);

    hex_to_num(payload, (int8_t *)buf);
    /*
     * Change message type to service ID
     */
    memcpy((uint8_t*)buf+21, &attach_code, sizeof(uint8_t));

    thread_state->si_other->sin_port = SERVICE_PORT;
    /*
     * Send service requests
     */
    put_enb_ue_s1ap_id((uint8_t*)buf+11, enb_ue_s1ap_id);

    printf("Sending Service request : %d\n",thread_state->thread_num);
    if (sendto(s, buf_start, BUFLEN, 0,(struct sockaddr *) thread_state->si_other, slen)==-1)
        diep("sendto()");
    /*
     * Start listening for auth/NAS requests
     */
    start = clock();
    while (1) {
        if (recvfrom(s, buf, BUFLEN, 0,(struct sockaddr *) thread_state->si_us, &slen)==-1) {
            printf("Thread %d died with thread state(%d)\n",
                   thread_state->thread_num, thread_state->state);
            err = ETIME;
            break;
        } else {
            /*
             * Process packet header
             * Check the type of the packet
             * After receiving packet, construct a packet and send it back
             */
            if (buf[0] == PACKET_ID_NAS_SEC_REQ) {
                printf("received service NAS request : %d\n",thread_state->thread_num);
		char payload[] = "000d40340000050000000200010008000480646dbe001a00090847f3914a9d00075e006440080002f83900e00000004340060002f8390001\0";

                memcpy(buf_start, &pkt_identifier, sizeof(pkt_identifier_t));
                buf = buf_start + sizeof(pkt_identifier_t);
                
                hex_to_num(payload,(int8_t *) buf);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, enb_ue_s1ap_id);
                
                if (sendto(s, buf_start, BUFLEN, 0, (struct sockaddr *)thread_state->si_other, slen)==-1)
                    diep("sendto()");
		
            } else if (buf[0] == PACKET_ID_AUTH_REQ) {
                printf("received service AUTH request : %d\n",thread_state->thread_num);
                
                char payload[] = "000d40370000050000000200010008000480646dbe001a000c0b075308deaaa8d6434c1b27006440080002f83900e00000004340060002f8390001\0";

                memcpy(buf_start, &pkt_identifier, sizeof(pkt_identifier_t));
                buf = buf_start + sizeof(pkt_identifier_t);
                
                hex_to_num(payload,(int8_t *) buf);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, enb_ue_s1ap_id);

                if (sendto(s, buf_start, BUFLEN, 0, (struct sockaddr *)thread_state->si_other, slen)==-1)
                    diep("sendto()");
            } else if (buf[0] == PACKET_ID_SERVICE_REQ_INITIAL_CONTEXT) {
                printf("received Initial context setup :%d\n",thread_state->thread_num);
                printf("\nSending setup response!!!! %d\n",thread_state->thread_num);
                char payload[] = "200900240000030000400200010008400480646dbe0033400f000032400a0a1f64640a5b47b28a9a\0";

                memcpy(buf_start, &pkt_identifier, sizeof(pkt_identifier_t));
                buf = buf_start + sizeof(pkt_identifier_t);
                
                hex_to_num(payload,(int8_t *)buf);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, enb_ue_s1ap_id);
		
    		end = clock();
		cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
		serv_time += cpu_time_used;
                if (sendto(s, buf_start, BUFLEN, 0,(struct sockaddr *) thread_state->si_other, slen)==-1)
                    diep("sendto()");
                close(s);
                return 0;
            }

        }

    }
    close(s);
    pthread_exit(&thread_state);
    return err;
}

static int
attach(void *arg)
{
    uint32_t            slen=sizeof(struct sockaddr_in);
    char                buf_array[BUFLEN], *buf_start, *buf;
    int                 err;
    thread_state_t      *thread_state = (thread_state_t*)arg;
#if DEF_CLOCK
    clock_t             start, end;
    double              cpu_time_used=0;
#elif DEF_GETTIMEOFDAY
    struct timeval t1, t2;
    struct timeval auth_recv, nas_recv;
    double              cpu_time_used=0;
#endif
    pkt_identifier_t    pkt_identifier;
    uint32_t            enb_ue_s1ap_id = 0;
    enb_ue_s1ap_id = (thread_state->thread_num + thread_state->thread_seed)* 10000 +
                    thread_state->serial_seed;

    char payload[] = "000c005c0000050008000480646dbe001a00323107417108298039100000111102802000200201d011271a8080211001000010810600000000830600000000000d00000a00004300060002f8390001006440080002f83900e000000086400130\0";

    /*
     * Lets put the pkt id in the very beginning
     */
    pkt_identifier.slice_id = 1;
    pkt_identifier.msg_type = PKT_TYPE_ATTACH;

    /* Keep the start pointer to use for sending
     */
    buf = buf_array;
    buf_start = buf;
    memcpy(buf_start, &pkt_identifier, sizeof(pkt_identifier_t));
    buf = buf_start + sizeof(pkt_identifier_t);

    hex_to_num(payload, (int8_t *)buf);
    increase_imsi_serial((uint8_t*)buf+24,thread_state->serial_seed);
    increase_imsi_thread((uint8_t*)buf+24,thread_state->thread_num + thread_state->thread_seed);
    print_imsi((uint8_t*)buf+24);
    put_enb_ue_s1ap_id((uint8_t*)buf+11, enb_ue_s1ap_id);
    /*
     * Send attach requests
     */
    getsockname(thread_state->socket, (struct sockaddr*)thread_state->si_us, &slen);

    
    if (sendto(thread_state->socket, buf_start, BUFLEN, 0,
               (struct sockaddr *) thread_state->si_other, slen)==-1)
        diep("sendto()");
#if DEF_CLOCK
    start = clock();
#elif DEF_GETTIMEOFDAY
    gettimeofday(&t1, NULL);
#endif
    increment_system_stat(&thread_state->thread_stats, 
                          STAT_ATTACH_ATTEMPT);

    /*
     * Start listening for auth/NAS requests
     */
    while (1) {
        if (recvfrom(thread_state->socket, buf, BUFLEN, 0,(struct sockaddr *) thread_state->si_us, &slen)==-1) {
            printf("Thread %d died with thread state: (%d)\n",
                   thread_state->thread_num, thread_state->state);
            err = ETIME;
            increment_system_stat(&thread_state->thread_stats, 
                                  STAT_ATTACH_FAIL);
            break;
        } else {
            /*
             * Process packet header
             * Check the type of the packet
             * After receiving packet, construct a packet and send it back
             */
            if (buf[0] == PACKET_ID_NAS_SEC_REQ) {
                printf("received NAS request : %d\n",thread_state->thread_num);
		char payload[] = "000d40340000050000000200010008000480646dbe001a00090847f3914a9d00075e006440080002f83900e00000004340060002f8390001\0";

                memcpy(buf_start, &pkt_identifier, sizeof(pkt_identifier_t));
                buf = buf_start + sizeof(pkt_identifier_t);

                hex_to_num(payload,(int8_t *) buf);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, enb_ue_s1ap_id);
                thread_state->state = STAT_ATTACH_NAS_REQ_RECV;
                increment_system_stat(&thread_state->thread_stats, 
                                      STAT_ATTACH_NAS_REQ_RECV);

#if DEF_GETTIMEOFDAY
                gettimeofday(&nas_recv, NULL);
                thread_state->thread_time_stats.attach_auth_send_to_nas_recv +=
                    (nas_recv.tv_sec - auth_recv.tv_sec) * 1000.0;
                thread_state->thread_time_stats.attach_auth_send_to_nas_recv +=
                    (nas_recv.tv_usec - auth_recv.tv_usec) / 1000.0;
#endif
                if (sendto(thread_state->socket, buf_start, 
                           BUFLEN, 0,(struct sockaddr *) thread_state->si_other, 
                           slen)==-1) {
                    diep("sendto()");
                } else {
                    thread_state->state = STAT_ATTACH_NAS_RESP_SENT;
                    increment_system_stat(&thread_state->thread_stats, 
                                          STAT_ATTACH_NAS_RESP_SENT);
                }
            } else if (buf[0] == PACKET_ID_AUTH_REQ) {
                printf("received AUTH request : %d\n",thread_state->thread_num);
                
                char payload[] = "000d40370000050000000200010008000480646dbe001a000c0b075308deaaa8d6434c1b27006440080002f83900e00000004340060002f8390001\0";
                
                memcpy(buf_start, &pkt_identifier, sizeof(pkt_identifier_t));
                buf = buf_start + sizeof(pkt_identifier_t);
                
                hex_to_num(payload,(int8_t *) buf);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, enb_ue_s1ap_id);
                thread_state->state = STAT_ATTACH_AUTH_REQ_RECV;
                increment_system_stat(&thread_state->thread_stats, 
                                      STAT_ATTACH_AUTH_REQ_RECV);
#if DEF_GETTIMEOFDAY
                gettimeofday(&auth_recv, NULL);
                thread_state->thread_time_stats.attach_initiate_to_auth_recv += 
                    (auth_recv.tv_sec - t1.tv_sec) * 1000.0;
                thread_state->thread_time_stats.attach_initiate_to_auth_recv += 
                    (auth_recv.tv_usec - t1.tv_usec) / 1000.0;
#endif

                if (sendto(thread_state->socket, buf_start, BUFLEN, 
                           0,(struct sockaddr *)thread_state->si_other, 
                           slen)==-1) {
                    diep("sendto()");
                } else {
                    thread_state->state = STAT_ATTACH_AUTH_RESP_SENT;
                    increment_system_stat(&thread_state->thread_stats, 
                                          STAT_ATTACH_AUTH_RESP_SENT);
                }
            } else if (buf[0] == PACKET_ID_ATTACH_ACCEPT) {
                printf("received ATTACH accept :%d\n",thread_state->thread_num);
#if DEF_CLOCK
		end = clock();
		cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
		total_time += cpu_time_used;
#elif DEF_GETTIMEOFDAY
                gettimeofday(&t2, NULL);
                cpu_time_used = (t2.tv_sec - t1.tv_sec) * 1000.0; 
                cpu_time_used += (t2.tv_usec - t1.tv_usec) / 1000.0;
                total_time    +=cpu_time_used;
                if (first_time_flag) {
                    rand_total_time = cpu_time_used;
                    rand_thread = thread_state->thread_num;
                    rand_serial = thread_state->serial_seed;
                    first_time_flag = 0;
                }
                thread_state->thread_time_stats.attach_total += 
                    cpu_time_used;
                thread_state->thread_time_stats.attach_nas_recv_to_accept += 
                    (t2.tv_sec - nas_recv.tv_sec) * 1000.0;
                thread_state->thread_time_stats.attach_nas_recv_to_accept += 
                    (t2.tv_usec - nas_recv.tv_usec) / 1000.0;
#endif

                printf("\nSending ATTACH complete!!!! %d\n",thread_state->thread_num);
                char payload[] = "000d40390000050000000200010008000480646dbe001a000e0d27e29c599901074300035200c2006440080002f83900e00000004340060002f8390001\0";

                memcpy(buf_start, &pkt_identifier, sizeof(pkt_identifier_t));
                buf = buf_start + sizeof(pkt_identifier_t);

                hex_to_num(payload,(int8_t *)buf);
                put_enb_ue_s1ap_id((uint8_t*)buf+18, enb_ue_s1ap_id);
                thread_state->state = STAT_ATTACH_ACCEPT_RECV;
                increment_system_stat(&thread_state->thread_stats, 
                                      STAT_ATTACH_ACCEPT_RECV);

                if (sendto(thread_state->socket, buf_start, 
                           BUFLEN, 0,(struct sockaddr *) thread_state->si_other, 
                           slen)==-1) {
                    diep("sendto()");
                } else {
                    thread_state->state = STAT_ATTACH_ACCEPT_COMPLETE_SENT;
                    increment_system_stat(&thread_state->thread_stats, 
                                          STAT_ATTACH_ACCEPT_COMPLETE_SENT);
                }
                return 0;
            } else {
                printf("\%d received garbage \n",thread_state->thread_num);

            }

        }

    }
    return err;
}

void *
execute_thread(void *arg)
{
    int retval, i;
    thread_state_t *thread_state = (thread_state_t*)arg;
    int                 s, ip_index;
    struct sockaddr_in  si_other, si_us;
    struct timeval tv;
#if DEF_GETTIMEOFDAY
#ifdef DEF_GET_ONE_SEC_CONN
    struct timeval t1, t2;   /* time code for 1 second connection count */
    double  elapsedTime=0;
    int     one_sec_flag = 1;
#endif
#endif
    tv.tv_sec = 2;
    tv.tv_usec = 0;

    if ((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP))==-1)
        diep("socket");

    //    memset((char *) &si_other, 0, sizeof(si_other));
    si_other.sin_family = AF_INET;
    si_other.sin_port = ATTACH_PORT ;
    //si_other.sin_addr.s_addr = inet_addr("5.5.5.6");
    si_other.sin_addr.s_addr = inet_addr(OTHER_IP);

    //    memset((char *) &si_us, 0, sizeof(si_us));
    si_us.sin_family = AF_INET;
    si_us.sin_port = htons(0);
    //si_us.sin_addr.s_addr = inet_addr("5.5.5.5");
    ip_index = thread_state->thread_num % (sizeof(iplist)/sizeof(iplist[0]));
    printf("Sending from: %s in %s\n",iplist[ip_index], __func__);
    si_us.sin_addr.s_addr = inet_addr(iplist[ip_index]);

    bind(s ,(struct sockaddr *)&si_us,sizeof(si_us));

    thread_state->socket = s;
    thread_state->si_other = &si_other;
    thread_state->si_us = &si_us;
    thread_state->udp_port = thread_state->si_us->sin_port;
    
    if (setsockopt(s, SOL_SOCKET, SO_RCVTIMEO,&tv,sizeof(tv)) < 0) {
            perror("Error");
            pthread_exit(&thread_state->state);
    }
    
#if DEF_GETTIMEOFDAY
#ifdef DEF_GET_ONE_SEC_CONN
    gettimeofday(&t1, NULL);
#endif
#endif
    for ( i = 0; i < serial_num; i++) {
        thread_state->serial_seed = i;
        retval = attach(arg);

#if DEF_GETTIMEOFDAY
#ifdef DEF_GET_ONE_SEC_CONN
        usleep(1000);
        gettimeofday(&t2, NULL);
        elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;
        elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;
        /*
         * If elapsed time is greater than 1 second
         * then print the number of connections handled till now
         */
        if (elapsedTime > 1000 && one_sec_flag) {
            printf("########## Total Conn in 1 sec: %d\n\n",i);
//            one_sec_flag = 0;
        }
#endif
#endif
        if (break_flag)
            break;

    }
    printf("Attach retval:%d\n",retval);
    printf("Lets sleep and then send service request: %d\n",thread_state->thread_num);
#if 0
    sleep(10);

    if (retval == 0) {
        retval = service_req(arg);
    }
#endif
    close(thread_state->socket);
    pthread_exit(&thread_state->state);
}

int main(int argc, char *argv[])
{
    pthread_t   *attach_thread;
    int         i=0, num_threads;
    int         seed = 0;
    thread_state_t       *thread_state;

    if (argc < 4) {
        printf("Usage: ./ue <number of ue Threads> <max serial conn> <Thread IMSI seed>\n");
        exit(0);
    }
    if (argc >= 4) {
        serial_num = atoi(argv[2]);
        seed = atoi(argv[3]);
    }

    num_threads = atoi(argv[1]);
    /*
     * Create n threads here each of which will take care of
     * its own entire entire attach procedure
     * After that wait for those threads to complete.
     */


    attach_thread = (pthread_t*)calloc(num_threads, sizeof(pthread_t));
    thread_state  = (thread_state_t*)calloc(num_threads, sizeof(thread_state_t));

    if (signal(SIGINT, sig_handler) == SIG_ERR) {
        printf("\ncan't catch SIGINT\n");
        return -1;
    }
    for (i=0; i<num_threads; i++) {
        thread_state[i].thread_num = i;
        thread_state[i].thread_seed = seed;
        pthread_create(&attach_thread[i], NULL, execute_thread, &thread_state[i]);
    }
    for (i=0; i<num_threads; i++) {
        pthread_join(attach_thread[i], NULL);
        accumulate_stat(&global_stats, &thread_state[i].thread_stats);
    }
    total_time = total_time/global_stats.attach_accept_complete_sent;
    serv_time = serv_time/global_stats.service_successful;

    show_system_global_stats();
    show_exit_counter_stats(&global_stats);
    show_time_thread_stats(thread_state, num_threads);
    show_system_thread_stats(thread_state, num_threads);
    show_time_global_stats();
    return 0;
}

