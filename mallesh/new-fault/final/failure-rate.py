import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10
tr = [10000, 20000, 30000, 40000, 50000]
tr = [i/1000 for i in tr]

sf = [9.35, 13.25, 19.12, 20.95, 23.45]
sl_cold = [0.75, 1.28, 2.35, 3.12, 3.75]
sl_hot = [0.15, 0.22, 0.44, 0.39, 0.57]
#oa = [0, 0.4, 0.6, 0.8, 0.9, 0.9, 0, 0, 0, 0, 0]
#op = [0, 0.2, 0.3, 0.8, 0.9, 0, 0, 0, 0, 0, 0]

plt.plot(tr, sf, linewidth=4, color='orange', ls='--', marker='^', markersize=14, label='Stateful Host/NF Failure')
plt.plot(tr, sl_cold, linewidth=4, color='navy', ls='--', marker='s', markersize=14, label='Stateless Cold Migration')
plt.plot(tr, sl_hot, linewidth=4, color='green', ls='--',  marker='D', markersize=14, label='Stateless Hot Migration')
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
