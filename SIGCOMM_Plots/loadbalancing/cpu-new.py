import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':60})
matplotlib.rcParams['figure.figsize'] = 14, 10

s1 = [1.25, 7.75, 5.25, 1.6, 1.25]
s2 = [16.65, 18.73, 14.72, 2.78, 1.25]

ind = np.arange(5)  # the x locations for the groups
width = 0.25
fig, ax1 = plt.subplots()

#fig.tight_layout()
#fig.subplots_adjust(left=0.1, bottom=0.4, right=0.95)

rects1 = ax1.bar(ind+0.1, s2, width, color='lightgreen', error_kw=dict(elinewidth=2,ecolor='sandybrown'), linewidth=4, capsize=10, label='50% Skew', hatch='/')
rects2 = ax1.bar(ind+width+0.15, s1, width, color='sandybrown', error_kw=dict(elinewidth=2,ecolor='sandybrown'), linewidth=4, capsize=10, label='Without Skew', hatch='.')

#plt.xticks(np.arange(len(s1))+0.15, ['RR', 'CH', 'Skewed-CH', 'ILP'])
#plt.xticks(np.arange(len(s1))+0.35, ['RR', 'CH', 'SK-CH', 'ILP'], fontsize='52')
plt.xticks(np.arange(len(s1))+0.35, ['RR', 'CH', 'Maglev', 'SK-CH', 'ILP'], fontsize='48')
plt.ylabel('Std Dev of Load Dist. (%)')
#ax1.grid(linestyle='--')
#plt.legend(loc=(0.01, 0.75),ncol=1)
#plt.legend(loc='upper right',ncol=1, fontsize=60, framealpha=None,borderpad=None, borderaxespad=None)
plt.legend(loc='upper right',ncol=1, fontsize=60, framealpha=None,borderpad=None, borderaxespad=None)
ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
ax1.xaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
plt.ylim([0, 33])
plt.yticks(range(0, 33, 10))
plt.savefig("./cpu-util-all.pdf", bbox_inches='tight')
plt.show()
