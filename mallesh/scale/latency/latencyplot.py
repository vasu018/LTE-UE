import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab

#data1 = [10.234, 18.448, 22.29, 28.204, 31.57, 39.45, 42.95]

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
count = 0
with open("./../scale_data.txt", "r") as ins:
    for line in ins:
        count = count +1

# Traffic Rate.
with open("./../nf_scale_data.txt", "r") as ins:
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
        txrate = float(words[1])
        nfcount = float(words[2])
        hostcount = float(words[3])
        latency = float(words[4])
        
        data3.append(float(x))
        data4.append(float(txrate))
        data5.append(float(nfcount))
        data6.append(float(hostcount))
        data7.append(float(latency))

fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()
ax3 = ax1.twinx()

ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('NF Scaling \n', color='m')
#ax2.set_ylabel('Host Scaling \n', color='r')
ax3.set_ylabel('Average Control Procedure Latency (msec)', color='b')

ax1.set_xlim([0,400])
ax1.set_xlabel('Time (sec)')
ax1.set_ylim([0,15])
#ax2.set_ylim([0,13])
ax3.set_ylim([0,500])

#ax1.plot(data3, data5, linewidth=3, linestyle='--', color='m', label='NF Scaling (#)')
ax1.plot(data1, data2, linewidth=3, linestyle='--', color='m', label='NF Scaling (#)')
#ax2.plot(data3, data6, linewidth=3, linestyle='--', color='r', label='Host Scaling (#)')
ax3.plot(data3, data7, linewidth=3, linestyle='--', color='b', label='Control Procedure Latency (msec)')

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')

plt.savefig("./latency-scale.pdf", bbox_inches='tight')
plt.show()
