import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

matplotlib.rcParams.update({'font.size':36})

means = [21.5, 20.5, 0.5, 3.25]

ind = np.arange(4)  # the x locations for the groups
width = 0.3
fig, ax1 = plt.subplots()
fig.tight_layout()
fig.subplots_adjust(left=0.1, bottom=0.2, right=0.99)

colors = ['lightgreen', 'lightgreen', 'lightblue', 'lightblue']
rects1 = ax1.bar(ind, means, width, edgecolor='k', linewidth=6, color=colors)
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

plt.xticks(np.arange(len(means)), ['Host\nFailure', 'Application\nFailure', 'Host\nFailure', 'Application\nFailure'])
plt.ylabel('Dropped Connections (%)')
ax1.grid(linestyle='--')
b_patch = mpatches.Patch(color='lightblue', label='Stateless')
g_patch = mpatches.Patch(color='lightgreen', label='stateful')
plt.legend(handles=[b_patch, g_patch])

plt.show()
