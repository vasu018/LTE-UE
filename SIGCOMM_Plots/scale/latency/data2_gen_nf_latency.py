#!/usr/bin/python
import random

# NF Scaling Plot.
nfcount = 1
hostcount = 1
latency = 10
lowlatency = 5
highlatency = 50

data1 = [10.234, 18.448, 22.29, 28.204, 31.57, 39.45, 42.95]


# Generate Latency Data.
f_latency = open('./latency_data.txt', 'w')

with open("./../scale_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        y = float(words[1])
        if (x == 21):
            #nfcount = nfcount +1
            latency = data1[0]
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
            nfcount = nfcount +1
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
        elif (x == 152):
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
            nfcount = nfcount - 1
        elif (x == 278):
            nfcount = nfcount - 1
        elif (x == 293):
            hostcount = hostcount - 1
            nfcount = nfcount - 1
        elif (x == 311):
            nfcount = nfcount - 1
        elif (x == 323):
            nfcount = 0        
        elif (x == 383):
            hostcount = hostcount - 1
        
        latency = random.randint(lowlatency,highlatency)
        f_latency.write(str(x) + "," + str(y) + "," + str(nfcount) + "," + str(hostcount) + "," + str(latency) + "\n")
        #print x, y, nfcount, hostcount, latency   
f_latency.close()
