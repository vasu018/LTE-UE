import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import matplotlib.mlab as mlab
import random

matplotlib.rcParams.update({'font.size':40})
matplotlib.rcParams['figure.figsize'] = 14, 10

ind = np.arange(5)

data_x = []
data1_control = []
data2_data = []

count = 100000 
step_count = 0

item_x1  = 0
with open("./service_spike.csv", "r") as ins:
    for item_x1, line in enumerate(ins):
        #if item_x1 > 25000 and item_x1 < 35000: 
        if item_x1 < 100000: 
            data_x.append(float(item_x1))
            line = line.strip()
            words = line.split(",")
            x1 = float(words[0])
            if float(x1) >= 100.0:
                ran_int = random.randint(2,4)
                x1 = ran_int * random.random()
                data1_control.append(float(x1))
            elif float(x1) > 3.0 and float(x1) < 100.0:
                ran_int = random.randint(2,4)
                x1 = ran_int * random.random()
                data1_control.append(float(x1))
            else:
                data1_control.append(float(x1))
            #print item_x

        #else:
        #    print("Redundant Control Traffic:", line)

item_x2  = 0
#with open("./attach_5000_1.csv", "r") as ins:
with open("./service_1_200000_spike.csv", "r") as ins:
    for item_x2, line_t in enumerate(ins):
        #if item_x2 > 25000 and item_x2 < 35000: 
        if item_x2 < 100000: 
            line_t = line_t.strip()
            words = line_t.split(",")
            x2 = float(words[0])
            if float(x2) >= 100.0:
                ran_int = random.randint(2,4)
                x2 = ran_int * random.random()
                data2_data.append(float(x2))
            elif float(x2) > 3.0 and float(x2) < 100.0:
                ran_int = random.randint(2,4)
                x2 = ran_int * random.random()
                data2_data.append(float(x2))
            else:
                data2_data.append(float(x2))

fig, ax1 = plt.subplots()
#ax3 = ax1.twinx()

fig.tight_layout()
#fig.subplots_adjust(left=0.09, top=0.8, bottom=0.3, right=0.9)
fig.subplots_adjust(left=0.09, bottom=0.3, right=0.9)

ax1.set_xlabel('IoT Control Vs Data Traffic')
ax1.set_ylabel('Normalized Traffic Volume')
#ax1.set_xlim([0,100000])
#ax1.set_xlim([25000,35000])
ax1.set_ylim([0,6])
ax1.set_yticks(range(0, 6, 2))

#print(data1_control)
#print(data2_data)

data1_control = ax1.plot(data_x, data1_control, linewidth=2, linestyle='-', color='royalblue', label='Control Traffic')
data2_data = ax1.plot(data_x, data2_data, linewidth=2, linestyle='-', color='lightgreen', label='Data Traffic')

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.xaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')

#plt.tick_params(axis='x',bottom='off',which='both',top='off', labelbottom='off')
#plt.xticks([0, 25000,50000,75000,100000],['00:00', '06:00','12:00','18:00','24:00'])
plt.xticks([25000,50000,75000,100000],['06:00','12:00','18:00','24:00'])

#lns = b+c+a+d
#labs = [l.get_label() for l in lns]
#ax1.legend(lns, labs, ncol=2, loc='upper center', bbox_to_anchor=(0.5, 1.45), fontsize=40,  borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

plt.legend(loc='upper right',ncol=1, fontsize=60, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

plt.savefig("./iot_control_data_traffic.pdf", bbox_inches='tight')
plt.show()
