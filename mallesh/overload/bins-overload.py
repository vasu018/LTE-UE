import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14, 10

data1 = []
with open("./manipulatedata/coloumn1.txt", "r") as ins:
    for line in ins:
	line = line.strip()
        words = line.split(",")  
        if words[0]:
            x = words[0]
        else:
            x = 0
        data1.append(float(x))


data2 = []
with open("./manipulatedata/coloumn3.txt", "r") as ins:
    for line in ins:
	line = line.strip()
        words = line.split(",")  
        if words[0]:
            x = words[0]
            x = float(x) * 10.0
        else:
            x = 0
        data2.append(float(x))

data3 = []
with open("./manipulatedata/coloumn18.txt", "r") as ins:
    for line in ins:
	line = line.strip()
        words = line.split(",")  
        if words[0]:
            x = words[0]
            x = float(x) * 2.8
        else:
            x = 0
        data3.append(float(x))

sampling = 0.5

data = []
c = 1
t = []
for i, j in zip(data1, data2):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += sampling

data = [2.6163952941176478, 6.14276079999999999, 45.933223399999996, 84.303287000000012, 81.385493599999975, 78.677416799999989, 79.917638199999999, 78.474943600000003, 84.800340599999984, 86.069941199999988, 53.458436199999994, 33.907551399999988, 20.917861200000004]

ax = plt.gca()

plt.plot(range(len(data)), data, marker='+', markersize=10, color='green', label='Src Host (TAU)')

data = []
c = 1
t = []
for i, j in zip(data1, data3):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += sampling

data = [5.5609795294117612, 6.0634179200000009, 9.8138712799999999, 8.0078698399999988, 7.0932653599999984, 6.0957836799999985, 6.0030740000000007, 7.2077175999999987, 9.3337489599999994, 8.1489461599999995, 5.8398306399999989, 5.742683519999999, 6.1557865600000001]
plt.plot(range(len(data)), data, marker='o', markersize=10, color='orange', label='Src Host (Migration)')

data4 = []
with open("./manipulatedata/coloumn1.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        if words[0]:
            x = words[0]
        else:
            x = 0
        #data1.append(float(x))
        data4.append(float(x))


data5 = []
with open("./manipulatedata/coloumn7.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        if words[0]:
            x = words[0]
            x = float(x) * 26.74
        else:
            x = 0
        data5.append(float(x))

data6 = []
with open("./manipulatedata/coloumn16.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        if words[0]:
            x = words[0]
            x = float(x) * 15.8
        else:
            x = 0
        data6.append(float(x))

data = []
c = 1
t = []
for i, j in zip(data4, data5):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += sampling

data = [5.4862177492156858, 5.3692090983999989, 29.659330543600001, 45.541586565999999, 43.633664569599993, 44.195828146399997, 45.055874788399997, 45.947195999600005, 43.511384590399999, 41.4871100951999994, 36.1964885443999993, 5.6787850307999994, 5.6232690471999991]
plt.plot(range(len(data)), data, marker='x', markersize=10, color='m', label='Dst Host (TAU)')

data = []
c = 1
t = []
for i, j in zip(data4, data6):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += sampling
data = [3.1379813058823527, 7.4215001120000004, 7.2806845079999998, 11.3901551240000005, 10.438342596, 12.439763648, 3.3874489000000008, 9.50292636, 8.5740440559999995, 4.4697624760000001, 6.2953330040000002, 5.2405142720000004, 3.473622416]
plt.plot(range(len(data)), data, marker='^', markersize=10, color='red', label='Dst Host (Migration)')

ax.set_ylim([0.1, 115])

plt.legend(loc='upper left', ncol=2, fontsize=26)
plt.xlabel('Time (sec)')
plt.ylabel('Average CPU Utilization (%)')

plt.grid(linestyle='--')
plt.savefig("./src-dst-cpu.pdf", bbox_inches='tight')
plt.show()
