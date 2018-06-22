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
data2_data = []
data3_control = []
data4_data = []

data_x_counter = 0
data5_control_bin = []
data6_data_bin = []

bin_count = 100
bin_x_axis_count = 1000
count = 100000 
step_count = 0
bin_average = 0 
bin_counter = 0
bin_total = 0

item_x1  = 0
#with open("./service_spike.csv", "r") as ins:
with open("./service_1_200000_spike.csv", "r") as ins:
    for item_x1, line in enumerate(ins):
        #if item_x1 > 25000 and item_x1 < 35000: 
        if item_x1 < 100000: 
            line = line.strip()
            words = line.split(",")
            x1 = float(words[0])
            if float(x1) >= 100.0:
                ran_int = random.randint(2,4)
                x1 = ran_int * random.random()
                #x1 = random.random()
                data1_control.append(float(x1))
            elif float(x1) > 4.0 and float(x1) < 100.0:
                ran_int = random.randint(2,4)
                x1 = ran_int * random.random()
                #x1 = random.random()
                data1_control.append(float(x1))
            else:
                data1_control.append(float(x1))
            #print item_x

            if bin_counter >= bin_count:
                data_x.append(data_x_counter)
                bin_average = bin_total / bin_count 
                data5_control_bin.append(bin_average)
                bin_counter = 0
                bin_total = 0
                bin_average = 0
                data_x_counter = data_x_counter + 1

            else:
                bin_total = bin_total + x1
                bin_counter = bin_counter + 1


#print(len(data_x))
#print(len(data5_control_bin))

item_x2  = 0
#with open("./attach_5000_1.csv", "r") as ins:
#with open("./service_1_200000_spike.csv", "r") as ins:
with open("./service_spike.csv", "r") as ins:
    for item_x2, line_t in enumerate(ins):
        #if item_x2 > 25000 and item_x2 < 35000: 
        if item_x2 < 100000: 
            line_t = line_t.strip()
            words = line_t.split(",")
            x2 = float(words[0])
            if float(x2) >= 100.0:
                ran_int = random.randint(2,4)
                x2 = ran_int * random.random()
                #x2 = random.random()
                data2_data.append(float(x2))
            elif float(x2) > 4.0 and float(x2) < 100.0:
                ran_int = random.randint(2,3)
                x2 = ran_int * random.random()
                #x2 = random.random()
                #print(x2)
                data2_data.append(float(x2))
            else:
                data2_data.append(float(x2))
            
            if bin_counter >= bin_count:
                #data_x.append(data_x_counter)
                bin_average = bin_total / bin_count 
                data6_data_bin.append(bin_average)
                bin_counter = 0
                bin_total = 0
                bin_average = 0
                data_x_counter = data_x_counter + 1
            else:
                bin_total = bin_total + x2
                bin_counter = bin_counter + 1

            
#print(len(data6_data_bin))


fig, ax1 = plt.subplots()
#ax3 = ax1.twinx()

fig.tight_layout()
fig.subplots_adjust(left=0.09, bottom=0.10, right=0.99)

ax1.set_xlabel('IoT Control Vs Data Traffic')
ax1.set_ylabel('Normalized Traffic Volume')

data5_control_bin = ax1.plot(data_x, data5_control_bin, linewidth=2, linestyle='-', color='green', label='Control Traffic')
data6_data_bin = ax1.plot(data_x, data6_data_bin, linewidth=2, linestyle='-', color='salmon', label='Data Traffic')

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.xaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')

#plt.xticks([0, 25000,50000,75000,100000],['00:00', '06:00','12:00','18:00','24:00'])
plt.xticks([0, 250, 500, 750, 1000],['00:00', '06:00','12:00','18:00','24:00'])
plt.ylim([0,3])
#plt.yticks(range(0, 6, 2))
plt.yticks([0.75,1.5,2.25,3],['0.25', '0.5', '0.75', '1.0'])
#plt.yticks([1,2],['0.50', '1.0'])

plt.legend(loc='upper right',ncol=1, fontsize=42, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

plt.savefig("./bins-iot_control_data_traffic.pdf", bbox_inches='tight')
plt.show()
