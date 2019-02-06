#ifndef UE_H
#define UE_H

#define BUFLEN 1024
#define NUM_UE 1
#define S1AP_PORT 2343
#define EXP_START_PORT 2355
#define EXP_STOP_PORT 2356
#define US_PORT 23432
#define RECPACK 10
#define OTHER_IP "10.10.10.30"
#define US_IP "10.10.10.185"

#define PACKET_ID_NAS_SEC_REQ   0x02
#define PACKET_ID_AUTH_REQ      0x03
#define PACKET_ID_ATTACH_ACCEPT 0x04
#define PACKET_ID_SERVICE_REQ_INITIAL_CONTEXT 0x04
#define PACKET_ID_DETACH_ACCEPT 0x05
#define PACKET_ID_DETACH_CONTEXT_RELEASE 0x06

//const char * const iplist[] = {"10.10.10.185", "10.10.10.186", "10.10.10.187"};
const char * const iplist[] = {"10.10.10.185"};

typedef struct udp_conn_context_s {
    int fd;
    struct sockaddr_in *si_other;
    struct sockaddr_in *si_us;
}udp_conn_context_t;

typedef enum {
    PKT_TYPE_ATTACH=0,
    PKT_TYPE_SERVICE,
    PKT_TYPE_DETACH,
    PKT_TYPE_TEST_MME
}pkt_type;

typedef struct pkt_identifier_s {
    uint8_t slice_id;
    uint8_t msg_type;
}pkt_identifier_t;

typedef enum {
    STAT_ATTACH_ATTEMPT = 0,
    STAT_ATTACH_NAS_REQ_RECV,
    STAT_ATTACH_NAS_RESP_SENT,
    STAT_ATTACH_AUTH_REQ_RECV,
    STAT_ATTACH_AUTH_RESP_SENT,
    STAT_ATTACH_ACCEPT_RECV,
    STAT_ATTACH_ACCEPT_COMPLETE_SENT,
    STAT_ATTACH_FAIL,

    STAT_SERVICE_ATTEMPT,
    STAT_SERVICE_NAS_REQ_RECV,
    STAT_SERVICE_NAS_RESP_SENT,
    STAT_SERVICE_AUTH_REQ_RECV,
    STAT_SERVICE_AUTH_RESP_SENT,
    STAT_SERVICE_ACCEPT_RECV,
    STAT_SERVICE_ACCEPT_COMPLETE_SENT,
    STAT_SERVICE_FAIL,

	STAT_DETACH_ATTEMPT,
	STAT_DETACH_FAIL,
	STAT_DETACH_ACCEPT,
	STAT_DETACH_CONTEXT_RELEASE
}stat_type;

typedef struct system_stats_s {
    unsigned long int     attach_attempt;
    unsigned long int     attach_auth_req_recv;
    unsigned long int     attach_auth_resp_sent;
    unsigned long int     attach_nas_req_recv;
    unsigned long int     attach_nas_resp_sent;
    unsigned long int     attach_accept_recv;
    unsigned long int     attach_accept_complete_sent;
    unsigned long int     attach_fail;

    unsigned long int     service_attempt;
    unsigned long int     service_auth_req_recv;
    unsigned long int     service_auth_resp_sent;
    unsigned long int     service_nas_req_recv;
    unsigned long int     service_nas_resp_sent;
    unsigned long int     service_accept_recv;
    unsigned long int     service_accept_complete_sent;
    unsigned long int     service_fail;
    
	unsigned long int     detach_attempt;
	unsigned long int     detach_accept;
	unsigned long int     detach_context_release;
	unsigned long int     detach_fail;
}system_stats_t;

typedef struct time_stats_s {
    double     attach_total;
    double     attach_initiate_to_auth_recv;
    double     attach_auth_send_to_nas_recv;
    double     attach_nas_recv_to_accept;

    double     service_total;
    double     service_initiate_to_auth_recv;
    double     service_auth_send_to_nas_recv;
    double     service_nas_recv_to_accept;
    
	double     detach_total;
	double     detach_send_to_accept_recv;
	double     detach_accept_to_context_release_recv;
}time_stats_t;

typedef struct thread_state_s {
    uint32_t    thread_num;
    uint32_t    udp_port;
    uint32_t    thread_seed;
    uint32_t    serial_seed;
    int         socket;
    int         state;
    system_stats_t  thread_stats;
    time_stats_t    thread_time_stats;
    struct sockaddr_in  *si_other;
    struct sockaddr_in  *si_us;
} thread_state_t;

#endif
