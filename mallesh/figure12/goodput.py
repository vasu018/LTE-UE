import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14, 10
tr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rc = [0, 1, 2, 3, 4, 4.76, 5.3, 5.35, 5.42, 5.42, 5.42]
sf = [0, 1, 2, 3, 4, 5, 5.95, 6.92, 7.74, 7.82, 7.82]
sl = [0, 1, 2, 3, 4, 5, 5.92, 6.85, 7.62, 7.64, 7.64]
oa = [0, 0.4, 0.6, 0.8, 0.9, 0.9, 0, 0, 0, 0, 0]
op = [0, 0.2, 0.3, 0.8, 0.9, 0, 0, 0, 0, 0, 0]

plt.plot(tr, sl, linewidth=3, color='orange', marker='^', markersize=12, label='Stateless')
plt.plot(tr, sf, linewidth=3, color='lightgreen', marker='o', markersize=12, label='Stateful')
plt.plot(tr, rc, linewidth=3, color='navy', marker='s', markersize=12, label='RamCloud')
plt.plot(tr[:2], oa[:2], linewidth=3, color='y', marker='D', markersize=12, label='OAI')
plt.plot(tr[:2], op[:2], linewidth=3, color='m', marker='*', markersize=12, label='OpenEPC')

plt.xlabel('Transmission Rate (Gbps)')
plt.ylabel('Goodput (Gbps)')

plt.legend(loc='upper left')
plt.ylim([0, 10])
plt.grid(linestyle='--')
plt.savefig("./goodput-fig12.pdf", bbox_inches='tight')
plt.show()
