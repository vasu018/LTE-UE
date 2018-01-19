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

#data1 = readXL('fault.xlsx', 2)
#data2 = readXL('fault.xlsx', 4)

#data1 = range(1, 101)
#data2 = []
#for i in data1:
#    data2.append(np.mean(data[(i-1)*100:i*100]))
#plt.plot(data1, data2)

#plt.scatter(data1, data2, marker='d', s=16, color='b', label='Service Latency')
data1 = readXL('fault.xlsx', 5)
#data1 = range(80, 101)
data2 = readXL('fault.xlsx', 7)
#data2 = []
#for i in data1:
#    data2.append(np.mean(data[(i-1)*100:i*100]))
#plt.plot(data1, data2)
plt.scatter(data1, data2, marker='o', facecolors='none', s=16, color='r', label='Re-attach Flood')
#

tfile = open('flood.txt', 'w')

for i, j in zip(data1, data2):
    tfile.write('%s\t'%(i))
    tfile.write('%s\n'%(j))

tfile.close()

ax.set_yscale('symlog')
ax.set_ylim([0.1, 50000])
ax.set_xlim([0, 100])

plt.legend(loc='upper left', ncol=3, fontsize=28)
plt.xlabel('Start Time (sec)')
plt.ylabel('Latency(ms)')

plt.show()
