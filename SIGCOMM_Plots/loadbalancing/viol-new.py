import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':60})
matplotlib.rcParams['figure.figsize'] = 14, 10

s1 = [3.62, 5.95, 3.24, 1.7, 1.25]
s2 = [17.25, 24.23, 16.23, 2.1, 1.25]
#stds1 = [5, 2, 1, 1]
#stds2 = [5, 2, 1, 1]

ind = np.arange(5)  # the x locations for the groups
width = 0.25
fig, ax1 = plt.subplots()
#fig.tight_layout()
#fig.subplots_adjust(left=0.1, bottom=0.4, right=0.95)

#rects1 = ax1.bar(ind, s2, width, edgecolor='k', color='gold', linewidth=6, capsize=10, label='50% skew')
#rects2 = ax1.bar(ind+width+0.05, s1, width, edgecolor='k', color='salmon', linewidth=6, capsize=10, label='Without Skew')

rects1 = ax1.bar(ind+0.1, s2, width, color='lightgreen', error_kw=dict(elinewidth=2,ecolor='lightgreen'), linewidth=4, capsize=10, label='50% Skew', hatch='/')
rects2 = ax1.bar(ind+width+0.15, s1, width, color='sandybrown', error_kw=dict(elinewidth=2,ecolor='sandybrown'), linewidth=4, capsize=10, label='Without Skew', hatch='.')

plt.xticks(np.arange(len(s1))+0.35, ['RR', 'CH', 'Maglev, SK-CH', 'ILP'])
plt.ylabel('Violations (%)')
ax1.grid(linestyle='--')
plt.legend(loc='upper right',ncol=1, fontsize=60, fancybox=True, framealpha=0.5)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.xaxis.grid(color='gray', linestyle='dashed')
plt.ylim([0, 40])
plt.yticks(range(0, 40, 10))
plt.savefig("./violations-all.pdf", bbox_inches='tight')
plt.show()
