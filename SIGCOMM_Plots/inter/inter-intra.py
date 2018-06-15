import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':60})
matplotlib.rcParams['figure.figsize'] = 14, 10

#s1 = [13.62, 15.92, 15.95, 13.24, 1.7, 1.35]
#s2 = [21.25, 28.2, 24.23, 18.53, 3.1, 1.51]
x = [a,b,c,d]
y = [7,9,23,25]
yyaxis
plot(x,y)

r = [3,2,3,4]
yyaxis 
plot(x,r)
fig, ax1 = plt.subplots()
ax3 = ax1.twinx()

ind = np.arange(6)  # the x locations for the groups
width = 0.25
fig.subplots_adjust(bottom=0.1, right=0.95)


rects2 = ax1.bar(ind+0.1, y, width, color='lightgreen', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='50% Skew', hatch='/')
rects1 = ax1.bar(ind+width+0.15, x, width, color='salmon', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='Without Skew', hatch='.')
rects3 = ax1.bar(ind+width+0.15, r, width, color='red', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='With Skew', hatch='*')


plt.xticks(np.arange(len(s1))+0.35, ['RR', 'PEPC', 'CH', 'Maglev'], fontsize='42')
plt.ylabel('Violations (%)')
ax1.grid(linestyle='--')
plt.legend(loc='upper right',ncol=1, fontsize=60, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
ax1.xaxis.grid(color='gray', linestyle='dashed')
ax1.yaxis.grid(color='gray', linestyle='dashed')
#plt.ylim([0, 41])
#plt.yticks(range(0, 41, 10))
plt.savefig("./inter-intra.pdf", bbox_inches='tight')
plt.show()
