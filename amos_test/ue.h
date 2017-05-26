#ifndef UE_H
#define UE_H

#define BUFLEN 1024
#define NUM_UE 1
#define ATTACH_PORT 2343
#define SERVICE_PORT 2343
#define US_PORT 23432
#define RECPACK 10
#define OTHER_IP "10.10.10.30"
#define US_IP "10.10.10.185"

#define PACKET_ID_NAS_SEC_REQ   0x02
#define PACKET_ID_AUTH_REQ      0x03
#define PACKET_ID_ATTACH_ACCEPT 0x04
#define PACKET_ID_SERVICE_REQ_INITIAL_CONTEXT 0x04

const char * const iplist[] = {"10.10.10.185"};

typedef struct udp_conn_context_s {
    int fd;
    struct sockaddr_in *si_other;
    struct sockaddr_in *si_us;
}udp_conn_context_t;

typedef enum {
    PKT_TYPE_ATTACH=0,
    PKT_TYPE_SERVICE,
    PKT_TYPE_DETACH
}pkt_type;


typedef struct pkt_identifier_s {
        uint8_t cluster_id;
        uint16_t hostid;
        uint16_t sliceid;
        uint16_t priorityid;
        uint8_t nextheader;
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
    STAT_SERVICE_SUCCESSFUL,
    STAT_SERVICE_FAIL
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
    unsigned long int     service_successful;
    unsigned long int     service_fail;
}system_stats_t;

typedef struct time_stats_s {
    double     attach_total;
    double     attach_initiate_to_auth_recv;
    double     attach_auth_send_to_nas_recv;
    double     attach_nas_recv_to_accept;

    double     service_attempt;
    double     service_successful;
    double     service_fail;
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
    uint16_t hostid;
} thread_state_t;

#endif
