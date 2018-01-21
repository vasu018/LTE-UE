import json
import os
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams.update({'font.size':18})


d11 = np.loadtxt('handover-mixed.txt', delimiter=',')
#d11 = [i+10 for i in d11]
d12 = np.loadtxt('service-mixed.txt', delimiter=',')
d12 = [i for i in d12 if i>0.5]

d21 = np.loadtxt('handover-niave-decomp.txt', delimiter=',')
#d21 = [i for i in d21 if i < 67]
d22 = np.loadtxt('service-niave-decomp.txt', delimiter=',')
d22 = [i for i in d22 if i>0.5]

d31 = [i for i in d21 if i<69]
d32 = [i+1+random.random()*16 for i in d22]

d41 = [i for i in d31 if i<55]
d42 = [i for i in d31 if i<17]


data_a = [d11, d21, d31, d41]
data_b = [d12, d22, d32, d42]

fig = plt.figure()
ax = fig.add_subplot(111)

fig.tight_layout()
fig.subplots_adjust(left=0.1, right=0.99)
#plt.xticks(rotation='90')

bp = ax.boxplot(data_a, 0, ' ', widths=0.1, positions=np.array(xrange(len(data_a)))*1.0-0.1, patch_artist=True)
bq = ax.boxplot(data_b, 0, ' ', widths=0.1, positions=np.array(xrange(len(data_a)))*1.0+0.1, patch_artist=True)
#bp = ax.boxplot(data_a, 0, ' ', widths=0.1, positions=np.array(xrange(len(data_a)))*1.0-0.1, boxprops=dict(linewidth=3), patch_artist=True)
#bq = ax.boxplot(data_b, 0, ' ', widths=0.1, positions=np.array(xrange(len(data_a)))*1.0+0.1, boxprops=dict(linewidth=3), patch_artist=True)

for patch in bq['boxes']:
    patch.set(facecolor='lightgreen')
for patch in bp['boxes']:
    patch.set(facecolor='lightblue')

ax.set_ylabel('Latency (ms)')
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['Unified MME', 'Naive\nDecomposition', 'Prioritization', 'Increased\nResource'])

#for box in bp['boxes']:
#    box.set( color='b', linewidth=3)
#
#for whisker in bp['whiskers']:
#    whisker.set(color='b', linewidth=3)
#
#for cap in bp['caps']:
#    cap.set(color='r', linewidth=3)
#
#for median in bp['medians']:
#    median.set(color='k', linewidth=2)

#ax.minorticks_on()
ax.grid(which='major', linestyle='--', linewidth='0.5')
#ax.grid(which='minor', linestyle='--', linewidth='0.5')
#ax.grid(which='major', linestyle='--', linewidth='0.5')
#ax.grid(which='minor', linestyle='--', linewidth='0.5')
plt.grid(linestyle='--')
plt.legend()
plt.ylim([-1, 100])
plt.savefig("./decomposition-f.pdf", bbox_inches='tight')
#plt.savefig("./decomposition-f.pdf")
plt.show()
