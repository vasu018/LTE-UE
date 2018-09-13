import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':75})
matplotlib.rcParams['figure.figsize'] = 14, 10

fig, ax1 = plt.subplots()
#line, = plt.plot([1,5,2,4], '-')
#line.set_dashes([8, 4, 2, 4, 2, 4])

#f = plt.figure()
#ax = f.add_subplot(111)
#fig, ax1 = plt.subplots()

#f.tight_layout()
#f.subplots_adjust(left=0.1, right=0.99)

tr = [10000, 20000, 30000, 40000, 50000]
tr = [i/1000 for i in tr]

#sf = [9.35, 13.25, 19.12, 20.95, 23.45]
sf = [7.35, 11.25, 19.12, 27.95, 43.45]
sl_cold = [1.25, 2.28, 3.35, 4.62, 6.75]
sl_hot = [0.66, 1.12, 1.74, 2.39, 3.97]

#plt.plot(tr, sf, linewidth=5, color='magenta', ls='--', marker='^', markersize=14, label='Stateful Host/NF Failure')
#plt.plot(tr, sl_cold, linewidth=5, color='maroon', ls='--', marker='s', markersize=14, label='Stateless Cold Migration')
#plt.plot(tr, sl_hot, linewidth=5, color='blue', ls='--', marker='D', markersize=14, label='Stateless Hot Migration')

plt.plot(tr, sf, marker='o', color='green', linewidth=12, markersize=18, linestyle='--', label='Stateful Session Restoration')
plt.plot(tr, sl_cold, marker='D', color='royalblue', linewidth=12, markersize=18, linestyle='--', label='Stateless Cold Migration')
plt.plot(tr, sl_hot, marker='s', color='tomato', linewidth=12, markersize=18, linestyle='--', label='Stateless Hot Migration')

plt.xlabel('# Control Procedures/Second')
plt.ylabel('Connection Failures (%)')

plt.legend(loc='upper left', fontsize=40, ncol=1, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
ax1.xaxis.grid(color='grey', linestyle='dashed')
ax1.yaxis.grid(color='grey', linestyle='dashed')

plt.xticks(tr, ['10k', '20k', '30k', '40k', '50k'])
plt.ylim([-1, 50])
plt.yticks(range(0, 51, 10))
#plt.legend(loc='upper left')
plt.grid(linestyle='--')
plt.savefig("./failure_rate_new.pdf", bbox_inches='tight')
plt.show()
