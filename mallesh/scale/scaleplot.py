import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
count = 0
with open("./scale_data.txt", "r") as ins:
    for line in ins:
        count = count +1

# Traffic Rate.
with open("./scale_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        data1.append(float(x))
        data2.append(float(y))

# NF Scaling Plot.
nfcount = 1
hostcount = 1
with open("./nf_scale_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        data3.append(float(x))
        data4.append(float(y))
        data5.append(float(z))
#plt.plot(data1, data2, linewidth=3, linestyle='--', color='r', label='Traffic Generation')
#plt.plot(data3, data4, linewidth=3, linestyle='--', color='b', label='NF Scaling')
#plt.ylim([0, 13000])

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(data1, data2, 'r--')
#ax2.plot(data3, data4, 'b--')
#ax2.plot(data3, data5, 'r--')

ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Traffic Generation', color='g')
ax2.set_ylabel('# NFs / Hosts (Scaling)', color='b')

#plt.plot(data1, data2, linewidth=3, linestyle='--', color='r', label='Traffic Generation')
plt.plot(data3, data4, linewidth=3, linestyle='--', color='b', label='NF Scaling')
#plt.ylim([0, 13000])
#plt.ylim([0, 130])
plt.xlim([0, 350])
ax1.set_ylim([0,13000])
ax2.set_ylim([0,13])

#plt.grid(linestyle='--')
plt.savefig("./scale-nf.pdf", bbox_inches='tight')
plt.show()




#
# Old Code
#
        
        #if (x == 13):
        #    nfcount = nfcount +1
        ##if (y == 2000):
        #elif (x == 23):
        #    nfcount = nfcount +1
        ##if (y == 3100):
        #elif (x == 34):
        #    nfcount = nfcount +1
        ##if (y == 3900):
        #elif (x == 44):
        #    nfcount = nfcount +1
        ##if (y == 4700):
        #elif (x == 55):
        #    nfcount = nfcount +1
        ##if (y == 5600):
        #elif (x == 67):
        #    nfcount = nfcount +1
        ##if (y == 6700):
        #elif (x == 79):
        #    hostcount = hostcount +1
        #    nfcount = nfcount +1
        ##if (y == 7900):
        #elif (x == 94):
        #    nfcount = nfcount +1
        ##if (y == 9200):
        #elif (x == 111):
        #    nfcount = nfcount +1
        ##elif (y == 10100):
        #elif (x == 121):
        #    nfcount = nfcount +1
        ##elif (y == 11200):
        #elif (x == 135):
        #    nfcount = nfcount +1
        #elif (x == 151):
        #    nfcount = nfcount - 1
        #elif (x == 176):
        #    nfcount = nfcount - 1
        #elif (x == 193):
        #    nfcount = nfcount - 1
        #elif (x == 211):
        #    nfcount = nfcount - 1
        #elif (x == 233):
        #    nfcount = nfcount - 1
        #elif (x == 257):
        #    nfcount = nfcount - 1
        #elif (x == 278):
        #    nfcount = nfcount - 1
        #elif (x == 298):
        #    nfcount = nfcount - 1
        #elif (x == 333):
        #    nfcount = nfcount - 1
        #elif (x == 373):
        #    nfcount = nfcount - 3
        #print x, y, nfcount, hostcount            
