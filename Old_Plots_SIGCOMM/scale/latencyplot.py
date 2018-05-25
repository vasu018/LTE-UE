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

# LAtency.
step_count = 0 
with open("./latency_datasf_sl_final.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        #txrate = words[1]
        nfcount = words[1]
        #hostcount = words[3]
        latency = words[2]
        latencysf = words[3]
        data1.append(float(x))
        data2.append(float(nfcount))
        data3.append(float(latency))
        data4.append(float(latencysf))
        #print x, nfcount, hostcount
        if step_count <= 6:
            #print dataLatency[step_count]
            step_count = step_count +1


fig, ax1 = plt.subplots()
ax3 = ax1.twinx()

fig.tight_layout()
fig.subplots_adjust(left=0.1, bottom=0.3, right=0.92)

ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('NF Scaling')
ax1.set_xlim([0,350])
ax1.set_ylim([0,15])
ax3.set_ylabel('Latency (ms)')
ax3.set_ylim([0,1000])
ax3.set_yscale('symlog')

a = ax1.plot(data1, data2, linewidth=5, linestyle='--', color='magenta', label='NF Scaling (#)')
b = ax3.plot(data1, data3, linewidth=3, linestyle='-.', marker='+', markersize=10 , color='blue', label='Stateless')
c = ax3.plot(data1, data4, linewidth=3, linestyle='-.', marker='+', markersize=10 , color='maroon', label='Stateful')

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')

lns = a+b+c
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, fontsize=36, loc='upper right')

plt.savefig("./latency-scale.pdf", bbox_inches='tight')
plt.show()
