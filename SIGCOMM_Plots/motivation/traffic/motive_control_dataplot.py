import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import matplotlib.mlab as mlab
import random

matplotlib.rcParams.update({'font.size':40})
matplotlib.rcParams['figure.figsize'] = 14, 10

dashList = [(5,2),(2,5),(4,10),(3,3,2,2),(5,5,20,5)]

ind = np.arange(5)

data_x = []
data1_control = []
data2_data = []
data3_control = []
data4_data = []

count = 100000 
step_count = 0 

item_x1  = 0
#with open("./service_spike.csv", "r") as ins:
with open("./service_1_200000_spike.csv", "r") as ins:
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
                #x1 = random.random()
                data1_control.append(float(x1))
            elif float(x1) > 4.0 and float(x1) < 100.0:
                ran_int = random.randint(2,3)
                x1 = ran_int * random.random()
                #x1 = random.random()
                data1_control.append(float(x1))
            else:
                data1_control.append(float(x1))
            #print item_x

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

average_control = 0
average_data = 0
control_val = 0
for control_val in data1_control:
    average_control = average_control + control_val
average_control = average_control / len(data1_control)

data_val = 0
for data_val in data2_data:
    average_data = average_data + data_val
average_data = average_data / len(data2_data)


#print average_control, average_data
#print len(data_x)
for idx1 in range(len(data1_control)):
    data3_control.append(float(average_control))


for idx2 in range(len(data2_data)):
    data4_data.append(float(average_data)) 

#print average_control, average_data

fig, ax1 = plt.subplots()
#ax3 = ax1.twinx()

fig.tight_layout()
#fig.subplots_adjust(left=0.09, top=0.8, bottom=0.3, right=0.9)
fig.subplots_adjust(left=0.09, bottom=0.10, right=0.99)

ax1.set_xlabel('IoT Control Vs Data Traffic')
ax1.set_ylabel('Normalized Traffic Volume')
#ax1.set_xlim([0,100000])
#ax1.set_xlim([25000,35000])
#ax1.set_ylim([0,4])
#ax1.set_yticks(range(0, 4, 1))

#print(data1_control)
#print(data2_data)

data1_control = ax1.plot(data_x, data1_control, linewidth=2, dashes=dashList[3], linestyle='-.', color='lightgreen', label='Control Traffic')
data2_data = ax1.plot(data_x, data2_data, linewidth=2, linestyle='-.', color='lightcoral', label='Data Traffic')
#data3_control = ax1.plot(data_x, data3_control, linewidth=6, linestyle='--', color='blue', label='Avg. Control Load')
#data4_data = ax1.plot(data_x, data4_data, linewidth=6, linestyle='--', color='red', label='Avg. Data Load')

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.xaxis.grid(color='gray', linestyle='dashed')
ax1.grid(True, which='both')

#plt.tick_params(axis='x',bottom='off',which='both',top='off', labelbottom='off')
#plt.xticks([0, 25000,50000,75000,100000],['00:00', '06:00','12:00','18:00','24:00'])
plt.xticks([0, 25000,50000,75000,100000],['00:00', '06:00','12:00','18:00','24:00'])
plt.yticks([1,2,3,4],['0.25','0.50','0.75','1.0'])

#lns = b+c+a+d
#labs = [l.get_label() for l in lns]
#ax1.legend(lns, labs, ncol=2, loc='upper center', bbox_to_anchor=(0.5, 1.45), fontsize=40,  borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

plt.legend(loc='upper right',ncol=2, fontsize=32, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

plt.savefig("./iot_control_data_traffic.pdf", bbox_inches='tight')
plt.show()
