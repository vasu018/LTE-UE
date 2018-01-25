import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab

#from mpl_toolkits.axes_grid1 import host_subplot
#import mpl_toolkits.axisartist as AA
#import matplotlib.pyplot as plt



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
ax3 = ax1.twinx()

#offset = 60
#new_fixed_axis = ax2.get_grid_helper().new_fixed_axis
#ax2.axis["right"] = new_fixed_axis(loc="right", axes=ax2,
#                                        offset=(offset, 0))

#ax2.axis["right"].toggle(all=True)


ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Traffic Generation (Gbps)', color='b')
ax2.set_ylabel('NF Scaling \n', color='m')
ax3.set_ylabel('Host Scaling \n', color='r')

#plt.xlim([0, 400])
ax1.set_xlim([0,399])
ax1.set_ylim([0,12000])
ax2.set_ylim([0,13])
ax3.set_ylim([0,13])

ax1.plot(data1, data2, linewidth=3, linestyle='--', color='b', label='Traffic Generation (Gbps)')
ax2.plot(data3, data4, linewidth=3, linestyle='--', color='m', label='NF Scaling (#)')
ax3.plot(data3, data5, linewidth=3, linestyle='--', color='r', label='Host Scaling (#)')

#plt.plot(data1, data2, linewidth=3, linestyle='--', color='r', label='Traffic Generation')
#plt.plot(data1, data2, linewidth=3, linestyle='--', color='b', label='Traffic Rate (Gbps)')
#plt.ylim([0, 13000])
#plt.ylim([0, 130])
#ax1.set_ylim([0,13000/1000])


ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
#ax.yaxis.grid(True)
ax1.grid(True, which='both')

#plt.grid(linestyle='--')
plt.savefig("./scale-nf.pdf", bbox_inches='tight')
plt.show()


