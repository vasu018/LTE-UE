import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14, 10

rr = [20.8, 9.4, 4.86, 3.2]
ch = [18.7, 7.6, 4.35, 3.81]
skch = [4.7, 2.6, 1.35, 1.11]
ilp = [3.5, 2.35, 1, 0.81]
hs = [3, 4, 5, 6]

plt.plot(hs, rr, marker='o', markersize='20', color='magenta', linewidth=4, linestyle='--', label='RR')
plt.plot(hs, ch, marker='s', markersize='20', color='orange', linewidth=4, linestyle='--', label='CH')
plt.plot(hs, skch, marker='^', markersize='20', color='blue', linewidth=4, linestyle='--', label='Skewed-CH')
plt.plot(hs, ilp, marker='*', markersize='20', color='maroon', linewidth=4, linestyle='--', label='ILP')

plt.xlabel('Number of Hosts')
plt.ylabel('Number of Violations (%)')
plt.xticks(hs, ['3', '4', '5', '6'])
plt.legend()
plt.grid(linestyle='--')
plt.savefig("./violations.pdf", bbox_inches='tight')
plt.show()
