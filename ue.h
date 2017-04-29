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

typedef struct udp_conn_context_s {
    int fd;
    struct sockaddr_in *si_other;
    struct sockaddr_in *si_us;
}udp_conn_context_t;

typedef struct thread_state_s {
    uint32_t     thread_num;
    uint32_t     udp_port;
    uint32_t     seed;
    int     nas_sec_recvd;
    int     auth_recvd;
    int     attach_complete_recvd;
    int     initial_context_setup;
    int     socket;
    struct sockaddr_in  *si_other;
    struct sockaddr_in  *si_us;
} thread_state_t;

#endif
