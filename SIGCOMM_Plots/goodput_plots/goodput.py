import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14,10 

fig, ax1 = plt.subplots()
fig.tight_layout()
fig.subplots_adjust(left=0.10, right=0.99)
dashList = [(5,2),(2,5),(4,10),(3,3,2,2),(5,5,20,5)]
tr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#rc = [0, 1, 2, 2.97, 3.89, 4.76, 5.3, 5.35, 5.42, 5.42, 5.42]
rc = [0, 1, 2, 2.97, 3.89, 4.89, 5.76, 6.35, 6.42, 6.22, 6.16]
sf = [0, 1, 2, 3, 4, 5, 5.95, 6.92, 7.84, 8.71, 8.81]
sl = [0, 1, 2, 3, 4, 5, 5.92, 6.85, 7.69, 8.27, 8.44]
oa = [0, 0.6, 1.1, 0.8, 0.9, 0.9, 0, 0, 0, 0, 0]
op = [0, 0.7, 0.9, 1.2, 0.9, 0, 0, 0, 0, 0, 0]

plt.plot(tr, sl, linestyle='--', linewidth=8, color='darkmagenta', marker='^', markersize=18, label='Stateless')
plt.plot(tr, sf, linestyle='--', linewidth=8, color='tomato', marker='s', markersize=18, label='Stateful')
plt.plot(tr, rc, linestyle='--', linewidth=8, color='seagreen', marker='o', markersize=18, label='RAMCloud')
plt.plot(tr[:3], oa[:3], linestyle='--', linewidth=8, color='royalblue', marker='D', markersize=18, label='OAI')
plt.plot(tr[:3], op[:3], linestyle='--', linewidth=8, color='firebrick', marker='*', markersize=18, label='OpenEPC')

#plt.plot(tr, sl, dashes=dashList[4], linestyle='--', linewidth=6, color='darkmagenta', marker='^', markersize=18, label='Stateless')
#plt.plot(tr, sf, dashes=dashList[4], linestyle='--', linewidth=6, color='royalblue', marker='s', markersize=18, label='Stateful')
#plt.plot(tr, rc, dashes=dashList[4], linestyle='--', linewidth=6, color='seagreen', marker='o', markersize=18, label='RamCloud')
#plt.plot(tr[:3], oa[:3], dashes=dashList[4], linestyle='--', linewidth=6, color='tomato', marker='D', markersize=18, label='OAI')
#plt.plot(tr[:3], op[:3], dashes=dashList[4], linestyle='--', linewidth=6, color='firebrick', marker='*', markersize=18, label='OpenEPC')

plt.xlabel('Transmission Rate (Gbps)', fontsize='34')
plt.ylabel('Goodput (Gbps)', fontsize='34')

plt.legend(loc='upper left', ncol=2, fontsize='36')
plt.ylim([0, 11])
plt.yticks(range(0, 11, 2))
plt.grid(linestyle='--')
plt.savefig("./goodput-fig12.pdf", bbox_inches='tight')
plt.show()
