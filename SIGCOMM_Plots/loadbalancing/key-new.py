import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':60})
matplotlib.rcParams['figure.figsize'] = 14, 10

s1 = [0.05, 10.4, 0.92, 0.4, 0.45]
s2 = [0.05, 10.8, 0.92, 3.78, 0.5]

ind = np.arange(5)  # the x locations for the groups
width = 0.25
fig, ax1 = plt.subplots()

#fig.tight_layout()
#fig.subplots_adjust(left=0.1, bottom=0.4, right=0.95)

rects1 = ax1.bar(ind+0.1, s2, width, color='lightgreen', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='50% Skew', hatch='/')
rects2 = ax1.bar(ind+width+0.15, s1, width, color='salmon', error_kw=dict(elinewidth=2,ecolor='sandybrown'), linewidth=2, capsize=10, label='Without Skew', hatch='.')

#plt.xticks(np.arange(len(s1))+0.15, ['RR', 'CH', 'Skewed-CH', 'ILP'])
#plt.xticks(np.arange(len(s1))+0.35, ['RR', 'CH', 'SK-CH', 'ILP'], fontsize='52')
plt.xticks(np.arange(len(s1))+0.35, ['RR', 'CH', 'Maglev', 'SK-CH', 'ILP'], fontsize='48')
plt.ylabel('Std Dev of Key Dist. (%)')
#ax1.grid(linestyle='--')
#plt.legend(loc=(0.01, 0.75),ncol=1)
plt.legend(loc='upper right',ncol=1, fontsize=60, fancybox=True, framealpha=0.5)
ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.xaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
plt.ylim([0, 19])
plt.yticks(range(0, 19, 5))
plt.savefig("./key-util-all.pdf", bbox_inches='tight')
plt.show()
