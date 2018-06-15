import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14, 10

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
data_sf = []
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
        data_sf.append(np.mean(t))
        t = []
        c += 0.1

#data3 = []
#data4 = []
#with open("./attach_flood_manipulated.txt", "r") as ins:
#    for line in ins:
#	line = line.strip()
#        words = line.split(",")  
#        x = words[0]
#        y = words[1]
#        data3.append(float(x))
#        data4.append(float(y))
#
#c = data3[20]
#t = []
#flood = []
#for i, j in zip(data3, data4):
#    t.append(j)
#    if i > c:
#        flood.append(np.mean(t))
#        t = []
#        c += 0.1

#plt.plot(range(37, 136), [i/1000 for i in flood], linewidth=1, marker='+', markersize=14, color='magenta', label='Restoration and Attach Flood')
#plt.scatter(range(200), [i/1000 for i in data], linewidth=1, marker='x', color='g', label='Stateful Host/NF Failure')
#plt.scatter(range(37, 136), [i/1000 for i in flood], linewidth=1, marker='+', s=100, color='magenta', label='Restoration and Attach Flood')

data3 = []
data4 = []
with open("./sl_nf_failure_data_modified.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        if float(x)>75 and float(x)<95:
            data3.append(float(x))
            data4.append(float(y))
c = 75
t = []
data_sl_nf = []
for i, j in zip(data3, data4):
    t.append(j)
    if i > c:
        data_sl_nf.append(np.mean(t))
        t = []
        c += 0.1

ax = plt.gca()


data5 = []
data6 = []
with open("./sl_host_failure_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        if float(x)>76 and float(x)<96:
            data5.append(float(x))
            data6.append(float(y))

c = 76
t = []
data_sl_host = []
for i, j in zip(data5, data6):
    t.append(j)
    if i > c:
        data_sl_host.append(np.mean(t))
        t = []
        c += 0.1

plt.plot(range(200), [i/1000 for i in data_sf], linewidth=1, marker='x', markersize=10, color='green', label='Stateful Host/NF Failure')
plt.plot(range(200), [i/1000 for i in data_sl_host], linewidth=1, marker='^', markersize=10, color='magenta', label='Stateless Host Failure')
plt.plot(range(200), [i/1000 for i in data_sl_nf], linewidth=1, marker='*', markersize=10, color='maroon', label='Stateless NF Failure')

#plt.xticks(np.arange(0, 225, 25), ['0', '5', '10', '15', '20', '25', '30', '35', '40'])
#plt.xticks(np.arange(0, 200, 25), ['0', '5', '10', '15', '20', '25', '30', '35', '40'])
plt.xticks(np.arange(0, 200, 25), ['0', '5', '10', '15', '20', '25', '30', '35', '40'])

plt.xlabel('Time (sec)',  fontsize='48')
plt.ylabel('Avg. Completion Time (sec)',  fontsize='48')
#plt.xlim([0, 30])
#plt.xticks(range(0, 30, 5))
plt.ylim([0, 5.2])
plt.yticks(range(0, 6, 2))
plt.grid(linestyle='--')
#plt.legend(ncol=1, fontsize=40)
plt.legend(loc='upper right',ncol=1, fontsize=42, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')
plt.savefig("./sf-nf-failure_new.pdf", bbox_inches='tight')
plt.show()
