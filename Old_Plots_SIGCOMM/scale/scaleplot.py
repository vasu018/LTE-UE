import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab
matplotlib.rcParams['figure.figsize'] = 20, 10

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

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax3 = ax1.twinx()

fig.tight_layout()
fig.subplots_adjust(left=0.1, bottom=0.3, right=0.92)

ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Traffic Generation (Gbps)')
ax2.set_ylabel('Host / NF Scaling (#)\n')

ax1.set_xlim([0,399])
ax1.set_ylim([0,14])
ax2.set_ylim([0,18])
ax3.set_ylim([0,18])

a = ax1.plot(data1, [i/1000 for i in data2], linewidth=5, linestyle='-.', color='orange', label='Traffic Generation (Gbps)')
b = ax2.plot(data3, data4, linewidth=5, linestyle='--', color='magenta', label='NF Scaling')
c = ax3.plot(data3, data5, linewidth=5, linestyle=':', color='green', label='Host Scaling')

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')

lns = a+b+c
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0, fontsize=34)

plt.savefig("./scale-nf.pdf", bbox_inches='tight')
plt.show()
