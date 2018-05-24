#!/usr/bin/python
import random

# NF Scaling Plot.

data1 = [10.234, 18.448, 22.29, 28.204, 31.57, 39.45, 42.95]

nfcount = 2 
hostcount = 1
latency = 5 
latencysf = 5 
lowlatency = 5
highlatency = 50

# Generate Scaling Data
f = open('./nf_scale_data.txt', 'w')

# Generate latency Data
flatency = open('./latency_data.txt', 'w')

# Generate latency Data one more copy
flatency2 = open('./latency_datasf_sl.txt', 'w')
flatency3 = open('./latency_datasf_sl_final.txt', 'w')

dataLatency = []
dataLatencysf = []
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
            latencysf = 5.87 + 1*random.random()   
        if (x == 21):
            nfcount = nfcount +1
            latency = 5 + 1*random.random()   
            latencysf = 5 + 1*random.random()   
            #latency = dataLatency[count-1] - 1*random.random()   
        #if (y == 2000):
        elif (x == 31):
            nfcount = nfcount +1
            latency = dataLatency[count-1] - 1*random.random()   
            latencysf = dataLatencysf[count-1] - 1*random.random()   
        #if (y == 3100):
        elif (x == 42):
            nfcount = nfcount +1
            latency = 4.9 + 1*random.random()   
            latencysf = 11.9 + 1*random.random()   
            #latency = dataLatency[count-1] - 1*random.random()   
        #if (y == 3900):
        elif (x == 52):
            nfcount = nfcount +1
            latency = 6.2 + 1*random.random()   
            latencysf = 9.2 + 1*random.random()   
            #latency = dataLatency[count-1] - 1*random.random()   
        #if (y == 4700):
        elif (x == 63):
            nfcount = nfcount +1
            latency = 6.8 + 1*random.random()   
            latencysf = 16.8 + 1*random.random()   
        #if (y == 5600):
        elif (x == 75):
            nfcount = nfcount +1
            latency = 7.8 + 1*random.random()   
            latencysf = 7.8 + 1*random.random()   
        #if (y == 6700):
        elif (x == 87):
            hostcount = hostcount +1
            nfcount = nfcount +2
            latency = 10.2 + 1*random.random()   
            latencysf = 124.2 + 10.3*random.random()   
        elif (x == 88):
            latencysf = 164.2 + 12.3*random.random()   
        elif (x == 89):
            latencysf = 189.2 + 13.3*random.random()   
        elif (x == 90):
            latencysf = 190.2 + 16.3*random.random()   
        elif (x == 91):
            latencysf = 193.2 + 16.3*random.random()   
        elif (x == 92):
            latencysf = 192.2 + 16.3*random.random()   
        elif (x == 93):
            latencysf = 188.2 + 16.3*random.random()   
        elif (x == 94):
            latencysf = 179.2 + 16.3*random.random()   
        elif (x == 95):
            latencysf = 164.2 + 16.3*random.random()   
        elif (x == 96):
            latencysf = 124.2 + 16.3*random.random()   
        elif (x == 97):
            latencysf = 132.2 + 16.3*random.random()   
        elif (x == 98):
            latencysf = 122.2 + 16.3*random.random()   
        elif (x == 98):
            latencysf = 97.2 + 16.3*random.random()   
        elif (x == 98):
            latencysf = 78.2 + 16.3*random.random()   
        elif (x == 98):
            latencysf = 53.2 + 16.3*random.random()   
        elif (x == 98):
            latencysf = 48.2 + 16.3*random.random()   
        elif (x == 100):
            latencysf = 22.2 + 16.3*random.random()   
        #if (y == 7900):
        elif (x == 102):
            nfcount = nfcount +1
            latency = 4.6 + 1*random.random()   
            latencysf = 4.6 + 1*random.random()   
        #if (y == 9200):
        elif (x == 119):
            nfcount = nfcount +1
            latency = 4.8 + 1*random.random()   
            latencysf = 9.8 + 1*random.random()   
        #elif (y == 10100):
        elif (x == 129):
            nfcount = nfcount +1
            latency = 5.9 + 1*random.random()   
            latencysf = 12.39 + 1*random.random()   
        #elif (y == 11200):
        #elif (x == 152):
        #    nfcount = nfcount -1
        elif (x == 161):
            nfcount = nfcount -1
            latency = 6.2 + 1*random.random()   
            latencysf = 63.2 + 1*random.random()   
        elif (x == 176):
            nfcount = nfcount - 1
            latency = 6.5 + 1*random.random()   
            latencysf = 70.23 + 1*random.random()   
        elif (x == 191):
            nfcount = nfcount - 1
            latency = 6.7 + 1*random.random()   
            latencysf = 83.2 + 1*random.random()   
        elif (x == 206):
            nfcount = nfcount - 1
            latency = 7.2 + 1*random.random()   
            latencysf = 82.73 + 1*random.random()   
        elif (x == 223):
            nfcount = nfcount - 1
            latency = 8.85 + 1*random.random()   
            latencysf = 79.85 + 1*random.random()   
        elif (x == 242):
            nfcount = nfcount - 1
            latency = 8.2 + 1*random.random()   
            latencysf = 68.2 + 1*random.random()   
        elif (x == 258):
            #nfcount = nfcount - 1
            hostcount = hostcount - 1
            nfcount = nfcount - 2 
            latency = 7.9 - 1*random.random()   
            latencysf = 57.9 - 1*random.random()   
        elif (x == 278):
            nfcount = nfcount - 1
            latency = 7.8 - 1*random.random()   
            latencysf = 7.8 - 1*random.random()   
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
            latencysf = 0
        elif (x==5):
            latency = 12.83965
            latencysf = 12.9 
        #elif (x >= 280 and x<= 290):
        #    #latency = 0
        #    latency = 1*random.random()
        elif (x >= 161):
            latency = latency - 0.31*random.random() 
            latencysf = latencysf - 0.55*random.random() 
        elif (x >= 278):
            #latency = 0
            latency = dataLatency[int(x-1)] - 2*random.random()
            latencysf = dataLatencysf[int(x-1)] - 2*random.random()
        else:
            #latency = latency + 3*random.random() 
            latency = latency + 0.25*random.random() 
            latencysf = latencysf + 0.5*random.random() 
            #print random.random()
            #latency = random.randint(lowlatency,highlatency)
            #print latency
            print latencysf
        f.write(str(x) + "," + str(nfcount) + "," + str(hostcount) + "\n")
        flatency.write(str(x) + "," + str(y) + "," + str(nfcount) + "," + str(hostcount) + "," + str(latency) + "," + str(latencysf) + "\n")
        #flatency2.write(str(x) + "," + str(latencysf) + "\n")
        flatency2.write(str(x) + "," + str(nfcount) + "," + str(latency) + "," + str(latencysf) + "\n")
        flatency3.write(str(x) + "," + str(nfcount) + "," + str(latency) + "," + str(latencysf) + "\n")
        dataLatency.append(float(latency))
        dataLatencysf.append(float(latencysf))
        print x, y, nfcount, hostcount, latency, latencysf   

f.close()
flatency.close()
flatency2.close()
flatency3.close()
