#!/usr/bin/python
import random

# NF Scaling Plot.

data1 = [10.234, 18.448, 22.29, 28.204, 31.57, 39.45, 42.95]

nfcount = 2 
hostcount = 1
latency = 10
lowlatency = 5
highlatency = 50

# Generate Scaling Data
f = open('./nf_scale_data.txt', 'w')

# Generate latency Data
flatency = open('./latency_data.txt', 'w')

with open("./scale_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        y = float(words[1])
        if (x == 21):
            nfcount = nfcount +1
        #if (y == 2000):
        elif (x == 31):
            nfcount = nfcount +1
        #if (y == 3100):
        elif (x == 42):
            nfcount = nfcount +1
        #if (y == 3900):
        elif (x == 52):
            nfcount = nfcount +1
        #if (y == 4700):
        elif (x == 63):
            nfcount = nfcount +1
        #if (y == 5600):
        elif (x == 75):
            nfcount = nfcount +1
        #if (y == 6700):
        elif (x == 87):
            hostcount = hostcount +1
            nfcount = nfcount +2
        #if (y == 7900):
        elif (x == 102):
            nfcount = nfcount +1
        #if (y == 9200):
        elif (x == 119):
            nfcount = nfcount +1
        #elif (y == 10100):
        elif (x == 129):
            nfcount = nfcount +1
        #elif (y == 11200):
        #elif (x == 152):
        #    nfcount = nfcount -1
        elif (x == 161):
            nfcount = nfcount -1
        elif (x == 176):
            nfcount = nfcount - 1
        elif (x == 191):
            nfcount = nfcount - 1
        elif (x == 206):
            nfcount = nfcount - 1
        elif (x == 223):
            nfcount = nfcount - 1
        elif (x == 242):
            nfcount = nfcount - 1
        elif (x == 258):
            #nfcount = nfcount - 1
            hostcount = hostcount - 1
            nfcount = nfcount - 2 
        elif (x == 278):
            nfcount = nfcount - 1
        elif (x == 293):
            nfcount = nfcount - 1
            #hostcount = hostcount - 1
            #nfcount = nfcount - 2 
        #elif (x == 297):
        #    nfcount = nfcount - 1
        elif (x == 311):
            nfcount = 2 
        elif (x == 323):
            nfcount = 0        
        #elif (x == 383):
        #    hostcount = hostcount - 1
        
        latency = random.randint(lowlatency,highlatency)
        f.write(str(x) + "," + str(nfcount) + "," + str(hostcount) + "\n")
        #print x, y, nfcount, hostcount, latency   

f.close()
