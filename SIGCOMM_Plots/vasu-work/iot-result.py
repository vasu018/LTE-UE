import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import matplotlib.mlab as mlab
import random

matplotlib.rcParams.update({'font.size':40})
matplotlib.rcParams['figure.figsize'] = 16, 12

dashList = [(5,2),(2,5),(4,10),(3,3,2,2),(5,5,20,5)]

ind = np.arange(5)

data_x = []
data1_control = []
data2_control = []
data3_control = []
data4_control = []

data_x_counter = 0
data1_control_bin = []
data2_control_bin = []
data3_control_bin = []
data4_control_bin = []

bin_count = 100 
bin_x_axis_count = 1000
#count = 10000 
step_count = 0
bin_average = 0 
bin_counter = 1 
bin_total = 0

item_x1  = 0
#with open("./service_spike.csv", "r") as ins:
with open("./special_out_dropcam", "r") as ins:
    for item_x1, line in enumerate(ins):
        #if item_x1 > 25000 and item_x1 < 35000: 
        if item_x1 < 100000: 
            line = line.strip()
            words = line.split(",")
            for word in words:
                data1_control_bin.append(word)
item_x1  = 0
with open("./special_out_printer", "r") as ins:
    for item_x1, line in enumerate(ins):
        #if item_x1 > 25000 and item_x1 < 35000: 
        if item_x1 < 100000: 
            line = line.strip()
            words = line.split(",")
            x1 = float(words[0])
            for word in words:
                data2_control_bin.append(float(x1))
            
print data2_control_bin
            
print(len(data1_control_bin))
print(len(data2_control_bin))


fig, ax1 = plt.subplots()
#ax3 = ax1.twinx()

fig.tight_layout()
fig.subplots_adjust(left=0.09, bottom=0.10, right=0.95)

ax1.set_xlabel('IoT Control Traffic')
ax1.set_ylabel('Normalized Traffic Volume')

data1_control_bin = ax1.plot(data_x, data1_control_bin, linewidth=2, linestyle='-', color='green', label='Drop Cam')
data2_control_bin = ax1.plot(data_x, data2_control_bin, linewidth=2, linestyle='-', color='salmon', label='Printer')
#data3_control_bin = ax1.plot(data_x, data3_control_bin, linewidth=2, linestyle='-', color='salmon', label='Category 3')

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.xaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')

#plt.xticks([0, 25000,50000,75000,100000],['00:00', '06:00','12:00','18:00','24:00'])
plt.xticks([0, 250, 500, 750, 1000],['00:00', '06:00','12:00','18:00','24:00'])
plt.ylim([0,3])
#plt.xlim([0,1000])
#plt.yticks(range(0, 6, 2))
plt.yticks([0.75,1.5,2.25,3],['0.25', '0.5', '0.75', '1.0'])
#plt.yticks([1,2],['0.50', '1.0'])

plt.legend(loc='upper right',ncol=1, fontsize=42, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

plt.savefig("./bins-iot_control_data_traffic_new.pdf", bbox_inches='tight')
plt.show()
