import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10

f = plt.figure()
ax = f.add_subplot(111)

f.tight_layout()
f.subplots_adjust(left=0.1, right=0.99)

def readXL(f, col):
    x = []
    workbook = xlrd.open_workbook(f)
    sheet = workbook.sheet_by_name('Sheet1')
    for value in sheet.col_values(col):
        if isinstance(value, float):
            x.append(value)
        else:
            x.append(0)
    return x

data1 = []
data2 = []
c = 1
data = []
with open("./sf_failure_data.txt", "r") as ins:
    for line in ins:
	line = line.strip()
        words = line.split(",")  
        x = words[0]
        y = words[1]
        if float(x) > 75 and float(x) < 95:
            data1.append(float(x))
            data2.append(float(y))

c = 75
t = []
for i, j in zip(data1, data2):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += 0.1

data3 = []
data4 = []
with open("./attach_flood_manipulated.txt", "r") as ins:
    for line in ins:
	line = line.strip()
        words = line.split(",")  
        x = words[0]
        y = words[1]
        data3.append(float(x))
        data4.append(float(y))

c = data3[20]
t = []
flood = []
for i, j in zip(data3, data4):
    t.append(j)
    if i > c:
        flood.append(np.mean(t))
        t = []
        c += 0.1

plt.plot(range(200), [i/1000 for i in data], linewidth=1, marker='x', markersize=14, color='g', label='Stateful Host/NF Failure')
plt.plot(range(37, 136), [i/1000 for i in flood], linewidth=1, marker='+', markersize=14, color='magenta', label='Restoration and Attach Flood')
#plt.scatter(range(200), [i/1000 for i in data], linewidth=1, marker='x', color='g', label='Stateful Host/NF Failure')
#plt.scatter(range(37, 136), [i/1000 for i in flood], linewidth=1, marker='+', s=100, color='magenta', label='Restoration and Attach Flood')

data1 = []
data2 = []
with open("./sl_nf_failure_data_modified.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        if float(x)>75 and float(x)<95:
            data1.append(float(x))
            data2.append(float(y))
c = 75
t = []
data = []
for i, j in zip(data1, data2):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += 0.1

ax = plt.gca()

plt.plot(range(200), [i/1000 for i in data], linewidth=1, marker='*', markersize=10, color='maroon', label='Stateless NF Failure')

data1 = []
data2 = []
with open("./sl_host_failure_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        if float(x)>76 and float(x)<96:
            data1.append(float(x))
            data2.append(float(y))

c = 76
t = []
data = []
for i, j in zip(data1, data2):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += 0.1

plt.plot(range(200), [i/1000 for i in data], linewidth=1, marker='^', markersize=12, color='gold', label='Stateless Host Failure')
plt.xticks(np.arange(0, 225, 25), ['0', '5', '10', '15', '20', '25', '30', '35', '40'])

plt.xlabel('Time (sec)')
plt.ylabel('Average Completion Time (sec)')
#plt.xlim([0, 20])
#plt.ylim([0, 5000])
plt.grid(linestyle='--')
plt.legend(ncol=1, fontsize=36)
plt.savefig("./sf-nf-failure.pdf", bbox_inches='tight')
plt.show()
