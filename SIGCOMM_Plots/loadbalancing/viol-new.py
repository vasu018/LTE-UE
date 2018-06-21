import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':60})
matplotlib.rcParams['figure.figsize'] = 16, 12

#s1 = [3.62, 5.95, 3.24, 1.7, 1.25]
s1 = [13.62, 17.12, 15.95, 13.24, 1.7, 1.35]
s2 = [21.25, 28.2, 24.23, 18.53, 3.1, 1.51]
#s3 = [28, 25.23, 19.53, 5.1, 3.51]

#stds1 = [5, 2, 1, 1]
#stds2 = [5, 2, 1, 1]

ind = np.arange(6)  # the x locations for the groups
width = 0.25
fig, ax1 = plt.subplots()
#fig.tight_layout()
fig.subplots_adjust(bottom=0.1, right=0.95)

#rects1 = ax1.bar(ind, s2, width, edgecolor='k', color='gold', linewidth=6, capsize=10, label='50% skew')
#rects2 = ax1.bar(ind+width+0.05, s1, width, edgecolor='k', color='salmon', linewidth=6, capsize=10, label='Without Skew')

rects2 = ax1.bar(ind+0.1, s2, width, color='lightgreen', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='50% Skew', hatch='/')
rects1 = ax1.bar(ind+width+0.15, s1, width, color='salmon', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='Without Skew', hatch='.')
#rects3 = ax1.bar(ind+width+width+0.20, s3, width, color='royalblue', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='PEPC', hatch='-')

plt.xlabel('LB schemes with MME')
plt.xticks(np.arange(len(s1))+0.35, ['RR', 'PEPC', 'CH', 'Maglev', 'MMLite', 'ILP'], fontsize='42')
plt.ylabel('Violations (%)')
ax1.grid(linestyle='--')
#plt.legend(loc='upper right',ncol=1, fontsize=60, fancybox=True, framealpha=0.5)
plt.legend(loc='upper right',ncol=1, fontsize=60, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
ax1.xaxis.grid(color='gray', linestyle='dashed')
ax1.yaxis.grid(color='gray', linestyle='dashed')
plt.ylim([0, 41])
plt.yticks(range(0, 41, 10))
plt.savefig("./violations-all_new.pdf", bbox_inches='tight')
plt.show()
