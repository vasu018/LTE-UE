#!/usr/bin/python
import random

# NF Scaling Plot.

nfcount = 1
hostcount = 1
latency = 10
lowlatency = 5
highlatency = 50

f = open('./nf_scale_data.txt', 'w')
f_latency = open('./latency_data.txt', 'w')

with open("./scale_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        y = float(words[1])
        if (x == 13):
            nfcount = nfcount +1
        #if (y == 2000):
        elif (x == 23):
            nfcount = nfcount +1
        #if (y == 3100):
        elif (x == 34):
            nfcount = nfcount +1
        #if (y == 3900):
        elif (x == 44):
            nfcount = nfcount +1
        #if (y == 4700):
        elif (x == 55):
            nfcount = nfcount +1
        #if (y == 5600):
        elif (x == 67):
            nfcount = nfcount +1
        #if (y == 6700):
        elif (x == 79):
            hostcount = hostcount +1
            nfcount = nfcount +1
        #if (y == 7900):
        elif (x == 94):
            nfcount = nfcount +1
        #if (y == 9200):
        elif (x == 111):
            nfcount = nfcount +1
        #elif (y == 10100):
        elif (x == 121):
            nfcount = nfcount +1
        #elif (y == 11200):
        elif (x == 135):
            nfcount = nfcount +1
        elif (x == 151):
            nfcount = nfcount - 1
        elif (x == 176):
            nfcount = nfcount - 1
        elif (x == 193):
            nfcount = nfcount - 1
        elif (x == 211):
            nfcount = nfcount - 1
        elif (x == 233):
            nfcount = nfcount - 1
        elif (x == 257):
            nfcount = nfcount - 1
        elif (x == 278):
            nfcount = nfcount - 1
        elif (x == 298):
            nfcount = nfcount - 1
        elif (x == 333):
            nfcount = nfcount - 1
        elif (x == 373):
            nfcount = nfcount - 3
        latency = random.randint(lowlatency,highlatency)
        f.write(str(x) + "," + str(nfcount) + "," + str(hostcount) + "\n")
        f_latency.write(str(x) + "," + str(nfcount) + "," + str(hostcount) + "," + str(latency) + "\n")
        print x, y, nfcount, hostcount    

f.close()
f_latency.close()
