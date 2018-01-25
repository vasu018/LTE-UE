import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10

data1 = []
data2 = []
with open("./sl_nf_failure_data_modified.txt", "r") as ins:
    for line in ins:
	line = line.strip()
        words = line.split(",")  
        x = words[0]
        y = words[1]
        if float(x)>60 and float(x)<100:
            data1.append(float(x))
            data2.append(float(y))
c = 60
t = []
data = []
for i, j in zip(data1, data2):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += 1

ax = plt.gca()

plt.plot(range(40), [i/1000 for i in data], linewidth=5, marker='o', markersize=18, color='blue')

plt.xlabel('Time (sec)')
plt.ylabel('Completion Time (sec)')

plt.grid(linestyle='--')
plt.savefig("./sl-nf-failure.pdf", bbox_inches='tight')
plt.show()
