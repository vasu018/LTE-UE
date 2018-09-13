import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})

rr = [20.8, 9.4, 4.86, 3.2]
ch = [18.7, 7.6, 4.35, 3.81]
hs = [3, 4, 5, 6]

plt.plot(hs, rr, marker='o', markersize='20', color='k', linewidth=4, linestyle='--', label='W-RR')
plt.plot(hs, ch, marker='s', markersize='20', color='orange', linewidth=4, linestyle='--', label='CH')

plt.xlabel('Number of Hosts')
plt.ylabel('Number of Violations (%)')
plt.xticks(hs, ['3', '4', '5', '6'])
plt.legend()
plt.grid(linestyle='--')
plt.show()
