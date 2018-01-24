import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':18})

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
        if float(x) > 0:
            data1.append(float(x))
            data2.append(float(y))

c = 1
t = []
for i in data1:
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


ax = plt.gca()

#plt.plot(data1, data)
plt.scatter(data1, data)

plt.legend(loc='upper left', ncol=3, fontsize=28)
plt.xlabel('Control Procedure Instantiation (sec)')
plt.ylabel('Completion Time (ms)')

plt.grid(linestyle='--')
#plt.savefig("./line-sf.pdf", bbox_inches='tight')
plt.show()
