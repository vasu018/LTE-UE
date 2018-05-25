import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14, 10

s1 = [1.25, 1.75, 1.9, 1.25]
s2 = [25.65, 22.73, 7.78, 1.25]

ind = np.arange(4)  # the x locations for the groups
width = 0.25
fig, ax1 = plt.subplots()

#fig.tight_layout()
#fig.subplots_adjust(left=0.1, bottom=0.4, right=0.95)

rects1 = ax1.bar(ind, s2, width, edgecolor='k', color='gold', linewidth=6, capsize=10, label='50% Skewed')
rects2 = ax1.bar(ind+width+0.05, s1, width, edgecolor='k', color='salmon', linewidth=6, capsize=10, label='Without Skew')

plt.xticks(np.arange(len(s1))+0.15, ['RR', 'CH', 'Skewed-CH', 'ILP'])
plt.ylabel('Std of CPU Utilization (%)')
ax1.grid(linestyle='--')
plt.legend()
plt.ylim([0, 30])
plt.savefig("./cpu-util-all.pdf", bbox_inches='tight')
plt.show()
