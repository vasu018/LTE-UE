#!/usr/bin/python
import random

# NF Scaling Plot.

data1 = [10.234, 18.448, 22.29, 28.204, 31.57, 39.45, 42.95]

nfcount = 2 
hostcount = 1
latency = 5 
lowlatency = 5
highlatency = 50

# Generate Scaling Data
f = open('./nf_scale_data.txt', 'w')

# Generate latency Data
flatency = open('./latency_data.txt', 'w')

dataLatency = []
with open("./scale_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        count = int(words[0])
        x = float(words[0])
        y = float(words[1])
        
        if (x == 11):
            #latency = dataLatency[count-1] - 1*random.random()   
            latency = 4.87 + 1*random.random()   
        if (x == 21):
            nfcount = nfcount +1
            latency = 5 + 1*random.random()   
            #latency = dataLatency[count-1] - 1*random.random()   
        #if (y == 2000):
        elif (x == 31):
            nfcount = nfcount +1
            latency = dataLatency[count-1] - 1*random.random()   
        #if (y == 3100):
        elif (x == 42):
            nfcount = nfcount +1
            latency = 4.9 + 1*random.random()   
            #latency = dataLatency[count-1] - 1*random.random()   
        #if (y == 3900):
        elif (x == 52):
            nfcount = nfcount +1
            latency = 6.2 + 1*random.random()   
            #latency = dataLatency[count-1] - 1*random.random()   
        #if (y == 4700):
        elif (x == 63):
            nfcount = nfcount +1
            latency = 6.8 + 1*random.random()   
        #if (y == 5600):
        elif (x == 75):
            nfcount = nfcount +1
            latency = 7.8 + 1*random.random()   
        #if (y == 6700):
        elif (x == 87):
            hostcount = hostcount +1
            nfcount = nfcount +2
            latency = 4.2 + 1*random.random()   
        #if (y == 7900):
        elif (x == 102):
            nfcount = nfcount +1
            latency = 4.6 + 1*random.random()   
        #if (y == 9200):
        elif (x == 119):
            nfcount = nfcount +1
            latency = 4.8 + 1*random.random()   
        #elif (y == 10100):
        elif (x == 129):
            nfcount = nfcount +1
            latency = 5.9 + 1*random.random()   
        #elif (y == 11200):
        #elif (x == 152):
        #    nfcount = nfcount -1
        elif (x == 161):
            nfcount = nfcount -1
            latency = 6.2 + 1*random.random()   
        elif (x == 176):
            nfcount = nfcount - 1
            latency = 7 + 1*random.random()   
        elif (x == 191):
            nfcount = nfcount - 1
            latency = 7.2 + 1*random.random()   
        elif (x == 206):
            nfcount = nfcount - 1
            latency = 7.73 + 1*random.random()   
        elif (x == 223):
            nfcount = nfcount - 1
            latency = 7.85 + 1*random.random()   
        elif (x == 242):
            nfcount = nfcount - 1
            latency = 8.2 + 1*random.random()   
        elif (x == 258):
            #nfcount = nfcount - 1
            hostcount = hostcount - 1
            nfcount = nfcount - 2 
            latency = 7.9 - 1*random.random()   
        elif (x == 278):
            nfcount = nfcount - 1
            latency = 7.8 - 1*random.random()   
        elif (x == 293):
            nfcount = nfcount - 1
            #hostcount = hostcount - 1
            #nfcount = nfcount - 2 
            #latency = 7.6 - 1*random.random() 
        #elif (x == 297):
        #    nfcount = nfcount - 1
        elif (x == 311):
            nfcount = 2 
        elif (x == 323):
            nfcount = 0        
        #elif (x == 383):
        #    hostcount = hostcount - 1
        if (x<=5):
            latency = 0
        elif (x==5):
            latency = 12.83965
        #elif (x >= 280 and x<= 290):
        #    #latency = 0
        #    latency = 1*random.random()
        elif (x >= 278):
            #latency = 0
            latency = dataLatency[int(x-1)] - 2*random.random()
        else:
            #latency = latency + 3*random.random() 
            latency = latency + 0.25*random.random() 
            #print random.random()
            #latency = random.randint(lowlatency,highlatency)
            print latency
        f.write(str(x) + "," + str(nfcount) + "," + str(hostcount) + "\n")
        flatency.write(str(x) + "," + str(y) + "," + str(nfcount) + "," + str(hostcount) + "," + str(latency) + "\n")
        dataLatency.append(float(latency))
        #print x, y, nfcount, hostcount, latency   

f.close()
flatency.close()
