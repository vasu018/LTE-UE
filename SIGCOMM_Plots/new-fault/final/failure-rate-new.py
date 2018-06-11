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

#sf = [9.35, 13.25, 19.12, 20.95, 23.45]
sf = [7.35, 11.25, 19.12, 27.95, 43.45]
sl_cold = [0.75, 1.28, 2.35, 3.62, 4.75]
sl_hot = [0.66, 1.12, 1.74, 2.39, 2.57]

plt.plot(tr, sf, linewidth=5, color='magenta', ls='--', marker='^', markersize=14, label='Stateful Host/NF Failure')
plt.plot(tr, sl_cold, linewidth=5, color='maroon', ls='--', marker='s', markersize=14, label='Stateless Cold Migration')
plt.plot(tr, sl_hot, linewidth=5, color='blue', ls='--', marker='D', markersize=14, label='Stateless Hot Migration')

plt.xlabel('# Control Procedures/Second')
plt.ylabel('Connection Failures (%)')

plt.xticks(tr, ['10k', '20k', '30k', '40k', '50k'])
plt.ylim([-1, 50])
plt.yticks(range(0, 51, 10))
plt.legend(loc='upper left')
plt.grid(linestyle='--')
plt.savefig("./failure_rate_new.pdf", bbox_inches='tight')
plt.show()
