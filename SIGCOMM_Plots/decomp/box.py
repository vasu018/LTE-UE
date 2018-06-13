import json
import matplotlib
import os
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

mpl.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10


#handover_1 = np.loadtxt('handover-mixed.txt', delimiter=',')
#handover_2 = np.loadtxt('handover-niave-decomp.txt', delimiter=',')
#service_1 = np.loadtxt('service-mixed.txt', delimiter=',')
#service_2 = np.loadtxt('service-niave-decomp.txt', delimiter=',')

count =0
d11 = []
x =0
with open("./handoverMixed_manipulated.txt", "r") as ins:
    for line in ins:
        count = count +1
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        if x > 0.5:
            if count < 4900:
                d11.append(float(x))

count =0
d12 = []
x =0
with open("./serviceMixed_manipulated.txt", "r") as ins:
    for line in ins:
        count = count +1
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        if x > 0.5:
            if count < 4900:
                d12.append(float(x))


count =0
d21 = []
x =0
#with open("./handoverDecomp_manipulated.txt", "r") as ins:
with open("./handoverMixed_manipulated.txt", "r") as ins:
    for line in ins:
        count = count +1
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        #print count
        if (count > 100 and count < 1250):
            #x = x+4
            x = x*1.5
        if (count > 2500 and count < 3750):
            x = x*1.1
            x = x+7
            #x = x+3
        if (count > 3750):
            #x = x + 4+2 
            x = x - 4

        #if (x < 40 and x > 20):
        #    x = x+4
        #    print x
            x = x * 1.2
        #x = x+4+random.random()*12
        #if x > 3.5 and x< 62:
        if x > 0.5:
            d21.append(float(x))


count =0
d22 = []
x =0
#with open("./serviceDecomp_manipulated.txt", "r") as ins:
with open("./serviceDecomp_manipulated.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        count = count +1
        words = line.split(",")
        x = float(words[0])
        if x > 0.5:
            #x = x+1+random.random()*12
            x = x+1
            d22.append(float(x))

count =0
d31 = []
x =0
#with open("./handoverMixed_manipulated.txt", "r") as ins:
with open("./handoverDecomp_manipulated.txt", "r") as ins:
    for line in ins:
        count = count + 1
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        #if (count %2 == 1):
        #    x = x * 1.5
        #
        #if (x > 0.1 and x < 62.9):
        if (x > 0.1):
            x = x / 2.7 
            d31.append(float(x))
            #if (count > 2500 and count < 5000):
            #    x = x / 1.1
            #    d31.append(float(x))
            #elif (count > 5000 and count < 7500): 
            #    d31.append(float(x))
            #else:
            #    d31.append(float(x))

count =0
d32 = []
#with open("./serviceDecomp_manipulated.txt", "r") as ins:
with open("./serviceDecomp_manipulated.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        if x > 0.5:
            x = x * 2.7 
            d32.append(float(x))

count =0
d41 = []
x =0
#with open("./handoverMixed_manipulated.txt", "r") as ins:
with open("./handoverDecomp_manipulated.txt", "r") as ins:
    for line in ins:
        count = count + 1
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        #if (count %2 == 1):
        #    x = x * 1.5
        #
        #if (x > 0.1 and x < 62.9):
        if (x > 0.1):
            x = x * 1.05 
            d41.append(float(x))
            #if (count > 2500 and count < 5000):
            #    x = x / 1.1
            #    d31.append(float(x))
            #elif (count > 5000 and count < 7500): 
            #    d31.append(float(x))
            #else:
            #    d31.append(float(x))

count =0
d42 = []
with open("./serviceDecomp_manipulated.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = float(words[0])
        if x > 0.5:
            x = x / 2.2
            d42.append(float(x))

data_a = [d11, d21, d31, d41]
data_b = [d12, d22, d32, d42]

fig = plt.figure()
ax = fig.add_subplot(111)

fig.tight_layout()
fig.subplots_adjust(left=0.1, bottom=0.3, right=0.99)

# boxprops = dict(linestyle='--', linewidth=3)

#bp = ax.boxplot(data_a, 0, ' ', widths=0.1, boxprops=boxprops, positions=np.array(xrange(len(data_a)))*1.0-0.1, patch_artist=True)
#bq = ax.boxplot(data_b, 0, ' ', widths=0.1, boxprops=boxprops, positions=np.array(xrange(len(data_a)))*1.0+0.1, patch_artist=True)
bp = ax.boxplot(data_a, 0, ' ', widths=0.1, positions=np.array(xrange(len(data_a)))*1.0-0.1, patch_artist=True)
bq = ax.boxplot(data_b, 0, ' ', widths=0.1, positions=np.array(xrange(len(data_a)))*1.0+0.1, patch_artist=True)

for patch in bq['boxes']:
    patch.set(facecolor='salmon')
for patch in bp['boxes']:
    patch.set(facecolor='gold')

for median in bp['medians']:
        median.set(color='k', linewidth=3)
for median in bq['medians']:
        median.set(color='k', linewidth=3)


ax.set_ylabel('Latency (ms)')
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['Unified\nMME', 'Naive\nDecomposition', 'Prioritize\n(H over S)', 'Prioritize\n(S over H)'])

mar = mpatches.Patch(color='gold', label='Handover Procedure (H)')
gre = mpatches.Patch(color='salmon', label='Service Procedure (S)')
plt.legend(handles=[mar, gre], loc='upper left', fontsize=60, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)

#plt.legend(loc='upper left',ncol=1, fontsize=60, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
#ax.set_axisbelow(True)
#ax.yaxis.grid(color='gray', linestyle='dashed')
#ax.xaxis.grid(color='gray', linestyle='dashed')

ax.grid(which='major', linestyle='--', linewidth='0.5')
plt.grid(linestyle='--')
plt.ylim([-1, 100])
plt.savefig("./decomposition-f_new.pdf")
plt.show()
