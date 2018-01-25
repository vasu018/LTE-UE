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
data6 = []
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
with open("./latency_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        nfcount = float(words[1])
        hostcount = float(words[2])
        latency = float(words[3])
        
        data3.append(float(x))
        data4.append(float(nfcount))
        data5.append(float(hostcount))
        data6.append(float(latency))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()

ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Traffic Generation (Gbps)', color='b')
ax2.set_ylabel('NF Scaling \n', color='m')
ax3.set_ylabel('Host Scaling \n', color='r')
ax4.set_ylabel('Average Control Procedure Latency (msec)', color='g')

ax1.set_xlim([0,400])
ax1.set_xlabel('Time (sec)')
ax1.set_xlim([0,399])
ax1.set_ylim([0,12000])
ax2.set_ylim([0,13])
ax2.set_ylim([0,13])
ax3.set_ylim([0,13])
ax4.set_ylim([0,5000])

ax1.plot(data1, data2, linewidth=3, linestyle='--', color='b', label='Traffic Generation (Gbps)')
ax2.plot(data3, data4, linewidth=3, linestyle='--', color='m', label='NF Scaling (#)')
ax3.plot(data3, data5, linewidth=3, linestyle='--', color='r', label='Host Scaling (#)')
ax4.plot(data3, data6, linewidth=3, linestyle='--', color='r', label='Control Procedure Latency (msec)')

#plt.scatter(data3, data6, linewidth=3, linestyle='--', color='b', label='Average Control Procedure Latency (msec)')

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')


plt.savefig("./latency-scale.pdf", bbox_inches='tight')
plt.show()
