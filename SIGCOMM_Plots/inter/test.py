import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':60})
matplotlib.rcParams['figure.figsize'] = 14, 10

fig, ax1 = plt.subplots()
#t = [1,2,3,4]
s1 = [7,9,23,25]
ax1.plot(s1, 'b-')
#ind = np.arange(6)
#width = 0.25

#ax1.set_xlabel('time (s)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('SD Resource', color='b')
ax1.tick_params('y', colors='b')

#rects2 = ax1.bar(ind+0.1, s1, width, color='lightgreen', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='50% Skew', hatch='/')
#rects1 = ax1.bar(ind+width+0.15, s2, width, color='blue', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='50% Skew', hatch='/')


plt.xticks(np.arange(len(s1))+0.35, ['RR+RR', 'Inter+RR', 'RR+Intra', 'Inter+Intra'], fontsize='42')

ax2 = ax1.twinx()
s2 = [4,6,12,17]
ax2.plot(s2, 'r.')
ax2.set_ylabel('SLO Violation', color='r')
ax2.tick_params('y', colors='r')

plt.savefig("./test.pdf", bbox_inches='tight')
plt.show()
#fig.tight_layout()
#plt.show()
