#ifndef UE_H
#define UE_H


#define BUFLEN 1024
#define NUM_UE 1
#define SRV_PORT 2343
#define CLIENT_PORT 23432
#define RECPACK 10
#define SRV_IP "5.5.5.6"
#define CLIENT_IP "5.5.5.5"

#define PACKET_ID_NAS_SEC_REQ   0x02
#define PACKET_ID_AUTH_REQ      0x03
#define PACKET_ID_ATTACH_ACCEPT 0x04

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
} thread_state_t;

#endif
