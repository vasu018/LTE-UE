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


int rrval = 1;
uint8_t ind = 0;
unsigned long int no_attach_req = 0;
unsigned long int no_attach_succ = 0;
unsigned long int no_serv_req = 0;
unsigned long int no_serv_succ = 0;
double total_time = 0;
double serv_time = 0;


void diep(char *s)
{
  perror(s);
//  pthread_exit(1);
  pthread_exit(&rrval);
}
/* diep(), #includes and #defines like in the server */
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

int
increase_imsi(uint8_t* imsi_p, int increment_val)
{
    int i;
    uint64_t ans=0;
    uint8_t *start = imsi_p +4; 
    uint32_t digit;

    for (i=0; i<4; i++) {
        ans = ans * 10;
        ans += (*start & 0xf0) >> 4;
        ans = ans * 10;
        ans += (*start & 0x0f);
        start += 1;
    }

    printf("increment imsi by = %d\n",increment_val);

    ans += increment_val;

    printf("last of imsi = %lu\n",ans);
    start = imsi_p+7;
    for (i=4; i>0; i--) {
        digit = ans % 10;
        ans = ans/10;
        *start = digit & 0x0f;

        digit = ans % 10;
        ans = ans/10;
        *start = *start | ((digit & 0x0f) << 4);
        start -= 1;
    }
    start++;
    *start = ind;
    return 0;
}

void *
service_req(void *arg)
{
    uint32_t            slen=sizeof(struct sockaddr_in);
    char                buf[BUFLEN];
    thread_state_t      *thread_state = (thread_state_t*)arg;
    int                 s = thread_state->socket;
    uint8_t             attach_code = 0x4d;
    clock_t start, end;
    double cpu_time_used=0;
    
    char payload[] = "000c005c0000050008000480646dbe001a00323107417108298039100000111102802000200201d011271a8080211001000010810600000000830600000000000d00000a00004300060002f8390001006440080002f83900e000000086400130\0";


    hex_to_num(payload, (int8_t *)buf);
    /*
     * Change message type to service ID
     */
    memcpy((uint8_t*)buf+21, &attach_code, sizeof(uint8_t));

    thread_state->nas_sec_recvd = 0;
    thread_state->auth_recvd = 0;
    thread_state->si_other->sin_port = SERVICE_PORT;
    /*
     * Send service requests
     */
//    put_enb_ue_s1ap_id((uint8_t*)buf+11, thread_state->udp_port);
    put_enb_ue_s1ap_id((uint8_t*)buf+11, thread_state->thread_num + thread_state->seed);

    printf("Sending Service request : %d\n",thread_state->thread_num);
    if (sendto(s, buf, BUFLEN, 0,(struct sockaddr *) thread_state->si_other, slen)==-1)
        diep("sendto()");
    /*
     * Start listening for auth/NAS requests
     */
	no_serv_req++;
    start = clock();
    while (1) {
        if (recvfrom(s, buf, BUFLEN, 0,(struct sockaddr *) thread_state->si_us, &slen)==-1) {
            printf("Thread %d died with thread state(nas_sec_req, auth_req, initial context) : (%d, %d, %d)\n",
                   thread_state->thread_num, thread_state->nas_sec_recvd,
                   thread_state->auth_recvd, thread_state->initial_context_setup);
            pthread_exit(0);
        } else {
            /*
             * Process packet header
             * Check the type of the packet
             * After receiving packet, construct a packet and send it back
             */
            if (buf[0] == PACKET_ID_NAS_SEC_REQ && (thread_state->nas_sec_recvd == 0)) {
                printf("received service NAS request : %d\n",thread_state->thread_num);
		char payload[] = "000d40340000050000000200010008000480646dbe001a00090847f3914a9d00075e006440080002f83900e00000004340060002f8390001\0";
                hex_to_num(payload,(int8_t *) buf);
//                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->udp_port);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->thread_num + thread_state->seed);
                thread_state->nas_sec_recvd = 1;
                
                if (sendto(s, buf, BUFLEN, 0, (struct sockaddr *)thread_state->si_other, slen)==-1)
                    diep("sendto()");
		
            } else if (buf[0] == PACKET_ID_AUTH_REQ && (thread_state->auth_recvd == 0)) {
                printf("received service AUTH request : %d\n",thread_state->thread_num);
                
                char payload[] = "000d40370000050000000200010008000480646dbe001a000c0b075308deaaa8d6434c1b27006440080002f83900e00000004340060002f8390001\0";
                hex_to_num(payload,(int8_t *) buf);
//                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->udp_port);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->thread_num + thread_state->seed);
                thread_state->auth_recvd = 1;

                if (sendto(s, buf, BUFLEN, 0, (struct sockaddr *)thread_state->si_other, slen)==-1)
                    diep("sendto()");
            } else if (buf[0] == PACKET_ID_SERVICE_REQ_INITIAL_CONTEXT && (thread_state->initial_context_setup == 0)) {
                printf("received Initial context setup :%d\n",thread_state->thread_num);
                printf("\nSending setup response!!!! %d\n",thread_state->thread_num);
                char payload[] = "200900240000030000400200010008400480646dbe0033400f000032400a0a1f64640a5b47b28a9a\0";
                hex_to_num(payload,(int8_t *)buf);
//                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->udp_port);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->thread_num + thread_state->seed);
                thread_state->initial_context_setup = 1;
		
		no_serv_succ ++;
    		end = clock();
		cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
		serv_time += cpu_time_used;
                if (sendto(s, buf, BUFLEN, 0,(struct sockaddr *) thread_state->si_other, slen)==-1)
                    diep("sendto()");
                close(s);

            }

        }

    }
    close(s);
    pthread_exit(0);
}

void *
attach(void *arg)
{
    uint32_t            slen=sizeof(struct sockaddr_in);
    char                buf[BUFLEN];
    struct sockaddr_in  si_other, si_us;
    int                 s;
    thread_state_t      *thread_state = (thread_state_t*)arg;
    struct timeval tv;
    tv.tv_sec = 2;
    tv.tv_usec = 0;
    clock_t start, end;
    double cpu_time_used=0;

    char payload[] = "000c005c0000050008000480646dbe001a00323107417108298039100000111102802000200201d011271a8080211001000010810600000000830600000000000d00000a00004300060002f8390001006440080002f83900e000000086400130\0";

    if ((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP))==-1)
        diep("socket");

    printf("Received fd : %d in %s\n",s, __func__);
    //    memset((char *) &si_other, 0, sizeof(si_other));
    si_other.sin_family = AF_INET;
    si_other.sin_port = ATTACH_PORT ;
    //si_other.sin_addr.s_addr = inet_addr("5.5.5.6");
    si_other.sin_addr.s_addr = inet_addr(OTHER_IP);

    //    memset((char *) &si_us, 0, sizeof(si_us));
    si_us.sin_family = AF_INET;
    si_us.sin_port = htons(0);
    //si_us.sin_addr.s_addr = inet_addr("5.5.5.5");
    si_us.sin_addr.s_addr = inet_addr(US_IP);

    bind(s ,(struct sockaddr *)&si_us,sizeof(si_us));

    thread_state->socket = s;
    thread_state->si_other = &si_other;
    thread_state->si_us = &si_us;

    if (setsockopt(s, SOL_SOCKET, SO_RCVTIMEO,&tv,sizeof(tv)) < 0) {
            perror("Error");
            pthread_exit(0);
    }

    hex_to_num(payload, (int8_t *)buf);
    increase_imsi((uint8_t*)buf+24,thread_state->thread_num + thread_state->seed);
    /*
     * Send attach requests
     */
    getsockname(s,(struct sockaddr*)&si_us,&slen);
    printf("Received fd : %d in %s\n",s , __func__);
    printf("Assigned port: %d\n",si_us.sin_port);

//    put_enb_ue_s1ap_id((uint8_t*)buf+11, si_us.sin_port);
    put_enb_ue_s1ap_id((uint8_t*)buf+11, thread_state->thread_num + thread_state->seed);
    thread_state->udp_port = si_us.sin_port;
    
    if (sendto(s, buf, BUFLEN, 0,(struct sockaddr *) &si_other, slen)==-1)
        diep("sendto()");
    
	no_attach_req++;
    start = clock();

    /*
     * Start listening for auth/NAS requests
     */
    while (1) {
        if (recvfrom(s, buf, BUFLEN, 0,(struct sockaddr *) &si_us, &slen)==-1) {
            printf("Thread %d died with thread state(nas_sec_req, auth_req, attach_accept) : (%d, %d, %d)\n",
                   thread_state->thread_num, thread_state->nas_sec_recvd,
                   thread_state->auth_recvd, thread_state->attach_complete_recvd);
            	printf("error number is %d %s\n",errno,strerror(errno));
		pthread_exit(0);
        } else {
            /*
             * Process packet header
             * Check the type of the packet
             * After receiving packet, construct a packet and send it back
             */
            if (buf[0] == PACKET_ID_NAS_SEC_REQ && (thread_state->nas_sec_recvd == 0)) {
                printf("received NAS request : %d\n",thread_state->thread_num);
		char payload[] = "000d40340000050000000200010008000480646dbe001a00090847f3914a9d00075e006440080002f83900e00000004340060002f8390001\0";
                hex_to_num(payload,(int8_t *) buf);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->thread_num + thread_state->seed);
//                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->udp_port);
                thread_state->nas_sec_recvd = 1;
                
                if (sendto(s, buf, BUFLEN, 0,(struct sockaddr *) &si_other, slen)==-1)
                    diep("sendto()");
		
            } else if (buf[0] == PACKET_ID_AUTH_REQ && (thread_state->auth_recvd == 0)) {
                printf("received AUTH request : %d\n",thread_state->thread_num);
                
                char payload[] = "000d40370000050000000200010008000480646dbe001a000c0b075308deaaa8d6434c1b27006440080002f83900e00000004340060002f8390001\0";
                hex_to_num(payload,(int8_t *) buf);
                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->thread_num + thread_state->seed);
//                put_enb_ue_s1ap_id((uint8_t*)buf+17, thread_state->udp_port);
                thread_state->auth_recvd = 1;

                if (sendto(s, buf, BUFLEN, 0,(struct sockaddr *) &si_other, slen)==-1)
                    diep("sendto()");
            } else if (buf[0] == PACKET_ID_ATTACH_ACCEPT && (thread_state->attach_complete_recvd == 0)) {
                printf("received ATTACH accept :%d\n",thread_state->thread_num);
		no_attach_succ++;
		end = clock();
		cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
		total_time += cpu_time_used;
                printf("\nSending ATTACH complete!!!! %d\n",thread_state->thread_num);
                char payload[] = "000d40390000050000000200010008000480646dbe001a000e0d27e29c599901074300035200c2006440080002f83900e00000004340060002f8390001\0";
                hex_to_num(payload,(int8_t *)buf);
//                put_enb_ue_s1ap_id((uint8_t*)buf+18, thread_state->udp_port);
                put_enb_ue_s1ap_id((uint8_t*)buf+18, thread_state->thread_num + thread_state->seed);
                thread_state->attach_complete_recvd = 1;

                if (sendto(s, buf, BUFLEN, 0,(struct sockaddr *) &si_other, slen)==-1)
                    diep("sendto()");

                printf("Lets sleep and then send service request: %d\n",thread_state->thread_num);

                sleep(10);
                service_req(thread_state);
            }

        }

    }
    close(s);
    pthread_exit(0);
}

int main(int argc, char *argv[])
{
	pthread_t   *attach_thread;
	int         i=0, num_ue;
	int         seed = 0;
	thread_state_t       *thread_state;

	if (argc < 2) {
		printf("Usage: ./ue <number of ue> <IMSI seed>\n");
		exit(0);
	}
	if (argc == 3) {
		seed = atoi(argv[2]);
	}

	num_ue = atoi(argv[1]);
	/*
	 * Create n threads here each of which will take care of
	 * its own entire entire attach procedure
	 * After that wait for those threads to complete.
	 */

	opterr = 0;

#if 0
	while ((c = getopt (argc, argv, "bs")) != -1)
		switch (c){
			case 'b':
				bflag = 1;
				break;
			case 's':
				sflag = 1;
				break;
			case '?':
				if (isprint (optopt))
					fprintf (stderr, "Unknown option `-%c'.\n", optopt);
				else
					fprintf (stderr,
							"Unknown option character `\\x%x'.\n",
							optopt);
				return 1;
			default:
				abort ();
		}    
#endif
	attach_thread = (pthread_t*)malloc(num_ue * sizeof(pthread_t));
	thread_state  = (thread_state_t*)malloc(num_ue * sizeof(thread_state_t));

	for (i=0; i<num_ue; i++) {
		thread_state[i].thread_num = i;
		thread_state[i].seed = seed;
		thread_state[i].nas_sec_recvd = 0;
		thread_state[i].auth_recvd = 0;
		thread_state[i].attach_complete_recvd = 0;
		pthread_create(&attach_thread[i], NULL, attach, &thread_state[i]);
	}
	for (i=0; i<num_ue; i++) {
		pthread_join(attach_thread[i], NULL);
	}
    if(no_attach_succ)
	total_time = total_time/no_attach_succ;
    if(no_serv_succ)
	serv_time = serv_time/no_serv_succ;

    printf("Number of attach req:%lu succ:%lu time:%f\n",no_attach_req,no_attach_succ,total_time);
    printf("Number of serv req:%lu succ:%lu time:%f\n",no_serv_req,no_serv_succ,serv_time);
    return 0;

}
