import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':60})
matplotlib.rcParams['figure.figsize'] = 16, 12

csfont = {'fontname':'Comic Sans MS', 'fontsize':'52'}
csfont2 = {'fontname':'Comic Sans MS', 'fontsize':'46'}
hfont = {'fontname':'Helvetica'}

f = plt.figure()
ax = f.add_subplot(111)

f.tight_layout()
f.subplots_adjust(left=0.12, right=0.975)

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
with open("./sf_failure_data.txt", "r") as ins:
    for line in ins:
	line = line.strip()
        words = line.split(",")  
        x = words[0]
        y = words[1]
        if (x > 70):
            data1.append(float(x))
            data2.append(float(y))


data3 = []
data4 = []
with open("./attach_flood_manipulated.txt", "r") as ins:
    for line in ins:
	line = line.strip()
        words = line.split(",")  
        x = words[0]
        y = words[1]
        if (x > 60):
            data3.append(float(x))
            data4.append(float(y))

data3 = [i-60 for i in data3]
data1 = [i-60 for i in data1]


plt.scatter(data1, data2, marker='d', s=20, color='g', label='Background Control')
plt.scatter(data3, data4, marker='o', s=20, facecolors='none', color='r', label='Restore and Attach')
#plt.scatter(data5, data6, marker='d', facecolors='none', s=16, color='b', label='No Host Failure')

ax.set_yscale('symlog')
#ax.set_yscale('symlog')
ax.set_ylim([0.1, 100000000])
#ax.set_xlim([0, 100])
ax.set_xlim([0, 40])

lgnd = plt.legend(loc='upper right', ncol=1, fontsize=52)
plt.xlabel('Time (sec)', csfont)
plt.ylabel('Finish Time (ms)', csfont)

plt.ylim((0,100000000))
#plt.yticks(fontsize=46)
#plt.yticks(range(0, 100000000, 10000000), fontsize=46)

#lgnd.legendHandles[0]._sizes = [80]
#lgnd.legendHandles[1]._sizes = [80]

plt.grid(linestyle='--')
plt.savefig("./legacy_ft_with_attach_flooding.pdf", bbox_inches='tight')
plt.show()
