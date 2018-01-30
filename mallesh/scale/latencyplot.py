import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab
matplotlib.rcParams['figure.figsize'] = 20, 10

dataLatency = [10.234, 18.448, 22.29, 28.204, 31.57, 39.45, 42.95]

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
count = 0
with open("./scale_data.txt", "r") as ins:
    for line in ins:
        count = count +1


step_count = 0 
# Traffic Rate.
with open("./latency_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        txrate = words[1]
        nfcount = words[2]
        hostcount = words[3]
        latency = words[4]
        data1.append(float(x))
        data2.append(float(txrate))
        data3.append(float(nfcount))
        data4.append(float(hostcount))
        data5.append(float(latency))
        print x, nfcount, hostcount
        if step_count <= 6:
            print dataLatency[step_count]
            step_count = step_count +1

fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()


fig.tight_layout()
fig.subplots_adjust(left=0.1, bottom=0.3, right=0.92)

ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('NF Scaling \n', color='k')
#ax2.set_ylabel('Host Scaling \n', color='r')
ax3.set_ylabel('Control Procedure Latency (msec)', color='k')

ax1.set_xlim([0,350])
ax1.set_xlabel('Time (sec)')
ax1.set_ylim([0,15])
#ax2.set_ylim([0,13])
#ax3.set_ylim([0,5000])
ax3.set_ylim([0,40])

#ax1.plot(data3, data5, linewidth=3, linestyle='--', color='m', label='NF Scaling (#)')
#ax2.plot(data1, data2, linewidth=3, linestyle='--', color='gold', label='Tx. Rate')
ax1.plot(data1, data3, linewidth=3, linestyle='--', color='m', label='NF Scaling (#)')
ax3.plot(data1, data5, linewidth=3, linestyle='-.', marker='+', markersize=10 , color='r', label='Control Procedure Latency (msec)')
ax4.plot(data1, data5, linewidth=3, linestyle='-.', marker='+', markersize=10 , color='r', label='Control Procedure Latency (msec)')

#plt.plot(range(37, 136), [i/1000 for i in flood], linewidth=1, marker='+', markersize=8, color='red', label='Restoration and Attach Flood')

#ax3.set_yscale('symlog')
ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')

plt.savefig("./latency-scale.pdf", bbox_inches='tight')
plt.show()
