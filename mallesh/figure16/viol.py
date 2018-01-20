import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':36})

means = [25, 22, 5]
stds = [5, 2, 1]

ind = np.arange(3)  # the x locations for the groups
width = 0.25
fig, ax1 = plt.subplots()
#fig.tight_layout()
#fig.subplots_adjust(left=0.1, bottom=0.4, right=0.95)

rects1 = ax1.bar(ind, means, width, edgecolor='k', color='tan', yerr=stds, linewidth=6, capsize=10)
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    la = ['4.3K', '250', '4.5M', '5.3M']
    c = 0
    for rect in rects:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., 1.05*height, la[c],
                #'%d' % int(height),
                ha='center', va='bottom', fontsize=24)
        c +=1

#autolabel(rects1)

plt.xticks(np.arange(len(means)), ['W-RR', 'CH', 'Skewed-CH'])
plt.ylabel('Violations (%)')
ax1.grid(linestyle='--')

plt.show()
