import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})

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

# Reattach Flood
data3 = readXL('fault.xlsx', 5)
data4 = readXL('fault.xlsx', 7)

# NO MME Host failure
data5 = readXL('fault.xlsx', 2)
data6 = readXL('fault.xlsx', 8)


data1 = []
data2 = []
with open("./sl_host_failure_data.txt", "r") as ins:
    for line in ins:
	line = line.strip()
        words = line.split(",")  
        x = words[0]
        y = words[1]
        data1.append(float(x))
        data2.append(float(y))

ax = plt.gca()
plt.scatter(data1, data2, marker='d', s=16, color='g', label='Host Failure Scenario')
#plt.scatter(data3, data4, marker='o', facecolors='none', s=16, color='r', label='Re-attach Flood')
#plt.scatter(data5, data6, marker='d', facecolors='none', s=16, color='b', label='No Host Failure')

ax.set_yscale('symlog')
ax.set_yscale('symlog')
ax.set_ylim([0.1, 50000])
ax.set_xlim([40, 100])

plt.legend(loc='upper left', ncol=3, fontsize=28)
plt.xlabel('Control Procedure Instantiation (sec)')
plt.ylabel('Completion Time (ms)')

plt.grid(linestyle='--')
plt.show()
