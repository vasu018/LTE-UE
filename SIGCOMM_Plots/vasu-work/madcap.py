from kamene.all import rdpcap
from kamene import *
from kamene.utils import PcapReader
from kamene.layers.inet import IP, TCP, UDP

import pandas as pd

class Counter:
    udp_data = 0
    udp_control = 0
    tcp_data = 0
    tcp_control = 0
    icmp_control = 0


LIST_OF_DEVICES = 'List of Devices'
MAC_ADDRESS = 'MAC ADDRESS'
CATEGORY = 'CATEGORY'
FIN = 0x01
SYN = 0x02

def read_device_list():
    df = pd.read_csv('List_Of_Devices.txt', header=0, sep='\t*', engine='python')
    df[LIST_OF_DEVICES] = df[LIST_OF_DEVICES].map(str.strip)
    df[MAC_ADDRESS] = df[MAC_ADDRESS].map(str.strip)
    print (len(df))
    df = df.assign(CATEGORY=['Hubs'] * 2 + ['Cameras'] * 7
                   + ['Switches & Triggers'] * 4
                   + ['Air quality sensors'] * 2
                   + ['Healthcare devices'] * 3
                   + ['Light bulbs']
                   + ['Electronics'] * 3
                   + ['Computers']
                   + ['Cameras'] + ['Computers'] * 6
                   + ['Router'])
    #print (df)
    return df

def set_key(df, p):
    #device_category = (df[df.iloc[:, 1] == str(p.src)][CATEGORY]).values[0]
    #return device_category
    return str(p.src) + str(p.dst)

def get_ip_addr(p):
    if IP in p:
        IPaddr = p[IP].src
    else:
        IPaddr = 0
    return IPaddr

def get_flags(p):
    if TCP in p:
        flags = p['TCP'].flags
        # print(flags, flags & FIN)

        if (flags & FIN):
            flags = 'FIN'
        elif (flags & SYN):
            flags = 'SYN'
        else:
            flags = 'TCP'
    elif UDP in p:
        flags = 'UDP'
    else:
        flags = 'ICMP'
    return flags

def read_pcap():
    df = read_device_list()
    base_time = 0
    hash_map = {}
    count = 0
    for p in PcapReader('16-09-23.pcap'):
        if (p.time - base_time > 5 * 60):
            if base_time > 0:
                print(len(hash_map))
                for key in hash_map:
                    src_device_name = (df[df.iloc[:, 1] == str(key[:17])][LIST_OF_DEVICES]).values[0]
                    #print(str(key[17:]))
                    try:
                       dst_device_name = (df[df.iloc[:, 1] == str(key[17:])][LIST_OF_DEVICES]).values[0]
                    except:
                       dst_device_name = str(key[17:])
                    print(count, src_device_name,
                          hash_map[key].udp_control + hash_map[key].tcp_control + hash_map[key].icmp_control, sep='|')
                    #      (src_device_name, key, hash_map[key].udp_data + hash_map[key].tcp_data,
                    #       hash_map[key].udp_control + hash_map[key].tcp_control
                    #       + hash_map[key].icmp_control)
            count += 1
            base_time = p.time
            hash_map = {}
        IPaddr = get_ip_addr(p)
        flags = get_flags(p)
        key = set_key(df, p)
        if key not in hash_map:
            hash_map[key] = Counter()

        if (flags =='SYN'):
            hash_map[key].tcp_data +=1
            hash_map[key].tcp_control += 1
        elif (flags == 'FIN'):
            hash_map[key].tcp_control += 1
        elif (flags == 'TCP'):
            hash_map[key].tcp_data += 1
        elif (flags == 'UDP'):
            if (hash_map[key].udp_control == 0):
                hash_map[key].udp_control = 2
            else:
                hash_map[key].udp_data += 1
        elif (flags == 'ICMP'):
            hash_map[key].icmp_control += 1

        #print(IPaddr, '|', device_name, '|', p.src, '|', p.dst, '|', p.time, '|', len(p), '|', flags)
        previousMAC = p.src

if __name__ == '__main__':
    read_pcap()
