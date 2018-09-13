import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10

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
        if float(x) > 60 and float(x) < 100:
            data1.append(float(x))
            data2.append(float(y))

c = 60
t = []
for i, j in zip(data1, data2):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += 1

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
        c += 1

ax = plt.gca()

plt.plot(range(40), [i/1000 for i in data], linewidth=5, marker='o', markersize=18, color='green', label='Host Failure')
plt.plot(range(18, 28), [i/1000 for i in flood], linewidth=5, marker='*', markersize=18, color='red', label='Re-attach Flood')

plt.xlabel('Time (sec)')
plt.ylabel('Completion Time (sec)')
plt.xlim([0, 40])
plt.ylim([0,5.5])
plt.grid(linestyle='--')


plt.legend()
plt.savefig("./sf-nf-failure.pdf", bbox_inches='tight')
plt.show()
