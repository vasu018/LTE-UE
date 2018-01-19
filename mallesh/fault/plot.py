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

data = np.loadtxt('flood.txt', delimiter='\t')
data1 = []
data2 = []

for i in data:
    data1.append(i[0])
    data2.append(i[1])


plt.scatter(data1, data2, marker='d', s=16, color='b', label='Service Latency')

ax.set_yscale('symlog')
ax.set_ylim([0.1, 50000])
ax.set_xlim([0, 100])

plt.legend(loc='upper left', ncol=3, fontsize=28)
plt.xlabel('Start Time (sec)')
plt.ylabel('Latency(ms)')

plt.show()
