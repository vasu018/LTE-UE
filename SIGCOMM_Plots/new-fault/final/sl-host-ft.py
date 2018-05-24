import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10

f = plt.figure()
ax = f.add_subplot(111)

f.tight_layout()
f.subplots_adjust(left=0.1, right=0.99)

data1 = []
data2 = []
with open("./sl_host_failure_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        if float(x)>75 and float(x)<95:
            data1.append(float(x))
            data2.append(float(y))

c = 75
t = []
data = []
for i, j in zip(data1, data2):
    t.append(j)
    if i > c:
        data.append(np.mean(t))
        t = []
        c += 0.1

plt.plot(range(200), [i/1000 for i in data], linewidth=1, marker='x', markersize=12, color='green')

plt.xticks(np.arange(0, 225, 25), ['0', '5', '10', '15', '20', '25', '30', '35', '40'])

plt.ylim([0,5.5])
plt.xlabel('Time (sec)')
plt.ylabel('Procedure Completion Time (sec)')

plt.grid(linestyle='--')
plt.savefig("./sl_host_ft.pdf", bbox_inches='tight')
plt.show()
