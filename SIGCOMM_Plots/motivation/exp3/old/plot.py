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

ax = plt.gca()

data1 = readXL('fault.xlsx', 2)
data2 = readXL('fault.xlsx', 4)
plt.scatter(data1, data2, marker='d', s=16, color='b', label='MME Down')
data1 = readXL('fault.xlsx', 5)
data2 = readXL('fault.xlsx', 7)
plt.scatter(data1, data2, marker='o', facecolors='none', s=16, color='r', label='Attach Flood')
data1 = readXL('fault.xlsx', 2)
data2 = readXL('fault.xlsx', 8)
plt.scatter(data1, data2, marker='+', s=16, color='g', label='MME Doesn\'t Fail')

ax.set_yscale('symlog')
ax.set_ylim([0.1, 50000])

plt.legend(loc='upper left', ncol=3, fontsize=28)
plt.xlabel('Start Time (sec)')
plt.ylabel('Latency(ms)')

plt.show()
