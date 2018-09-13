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

print len(data), len(flood)

ax = plt.gca()

plt.plot(range(200), [i/1000 for i in data], linewidth=5, marker='o', markersize=18, color='maroon', label='Service Requests')
plt.plot(range(35, 134), [i/1000 for i in flood], linewidth=5, marker='o', markersize=18, color='green', label='Re-attach Flood')

plt.xlabel('Control Procedure Instantiation (sec)')
plt.ylabel('Completion Time (sec)')
plt.xlim([0, 200])
plt.grid(linestyle='--')
plt.legend()
plt.savefig("./bins-line-sf.pdf", bbox_inches='tight')
plt.show()
