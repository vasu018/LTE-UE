import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':40})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab
matplotlib.rcParams['figure.figsize'] = 20, 10

dataLatency = [10.234, 18.448, 22.29, 28.204, 31.57, 39.45, 42.95]

data_x = []
data1_control = []
data2_data = []

count = 100000 
step_count = 0

item_x  = 0
with open("./service_spike.csv", "r") as ins:
    for item_x, line in enumerate(ins):
        if item_x < 100000: 
            data_x.append(float(item_x))
            line = line.strip()
            words = line.split(",")
            x = words[0]
            data1_control.append(float(x))
            #print item_x

        #else:
        #    print("Redundant Control Traffic:", line)
print(len(data_x))
print(len(data1_control))

item_x  = 0
#with open("./attach_5000_1.csv", "r") as ins:
with open("./service_1_200000_spike.csv", "r") as ins:
    for item_x, line in enumerate(ins):
        if item_x < 100000: 
            line = line.strip()
            words = line.split(",")
            x = words[0]
            data2_data.append(float(x))
        #else:
        #    print("Redundant Data Traffic:", line)

print(len(data_x))
print(len(data1_control))

fig, ax1 = plt.subplots()
#ax3 = ax1.twinx()

fig.tight_layout()
#fig.subplots_adjust(left=0.09, top=0.8, bottom=0.3, right=0.9)
fig.subplots_adjust(left=0.09, bottom=0.3, right=0.9)

ax1.set_xlabel('IoT Control Vs Data Traffic')
ax1.set_ylabel('Normalized Traffic Volume')
ax1.set_xlim([0,5000])
ax1.set_ylim([0,15])
ax1.set_yticks(range(0, 3, 1))

data1_control = ax1.plot(data_x, data1_control, linewidth=4, linestyle='--', color='royalblue', label='Control Traffic')
data2_data = ax1.plot(data_x, data2_data, linewidth=4, linestyle='--', color='lightgreen', label='Data Traffic')

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.xaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')

#lns = b+c+a+d
#labs = [l.get_label() for l in lns]
#ax1.legend(lns, labs, ncol=2, loc='upper center', bbox_to_anchor=(0.5, 1.45), fontsize=40,  borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

plt.legend(loc='upper right',ncol=1, fontsize=60, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

plt.savefig("./motive_control_data.pdf", bbox_inches='tight')
plt.show()
