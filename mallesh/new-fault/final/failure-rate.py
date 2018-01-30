import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10

f = plt.figure()
ax = f.add_subplot(111)

f.tight_layout()
f.subplots_adjust(left=0.1, right=0.99)

tr = [10000, 20000, 30000, 40000, 50000]
tr = [i/1000 for i in tr]

sf = [9.35, 13.25, 19.12, 20.95, 23.45]
sl_cold = [0.75, 1.28, 2.35, 3.62, 4.75]
sl_hot = [0.66, 1.12, 1.74, 2.39, 2.57]
#oa = [0, 0.4, 0.6, 0.8, 0.9, 0.9, 0, 0, 0, 0, 0]
#op = [0, 0.2, 0.3, 0.8, 0.9, 0, 0, 0, 0, 0, 0]

plt.plot(tr, sf, linewidth=4, color='green', ls='--', marker='^', markersize=14, label='Stateful Host/NF Failure')
plt.plot(tr, sl_cold, linewidth=4, color='blue', ls='--', marker='s', markersize=14, label='Stateless Cold Migration')
plt.plot(tr, sl_hot, linewidth=4, color='magenta', ls='--', marker='D', markersize=14, label='Stateless Hot Migration')
#plt.plot(tr[:2], oa[:2], linewidth=3, color='y', marker='D', markersize=12, label='OAI')
#plt.plot(tr[:2], op[:2], linewidth=3, color='m', marker='*', markersize=12, label='OpenEPC')

plt.xlabel('# Control Procedures Per Second')
plt.ylabel('% Connection Reattaches / Failures')

plt.xticks(tr, ['10k', '20k', '30k', '40k', '50k'])
plt.ylim([-1, 30])

plt.legend(loc='upper left')
plt.grid(linestyle='--')
plt.savefig("./failure_rate.pdf", bbox_inches='tight')
plt.show()
