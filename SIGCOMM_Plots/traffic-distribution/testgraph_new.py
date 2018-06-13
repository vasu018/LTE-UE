import numpy as np
import matplotlib
import matplotlib.pyplot as plt

csfont = {'fontname':'Comic Sans MS', 'fontsize':'52'}
csfont2 = {'fontname':'Comic Sans MS', 'fontsize':'46'}
hfont = {'fontname':'Helvetica'}
dashList = [(5,2),(2,5),(4,10),(3,3,2,2),(5,5,20,5)]

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14, 10

fig, ax1 = plt.subplots()
fig.tight_layout()
fig.subplots_adjust(left=0.12, right=0.99)


approach1_new = [1,1,1,1,1,1,1,1]
approach2_new = [1,0.9,0.8,0.7,0.7,0.7,0.7,0.7]
approach3_new = [1,0.8,0.6,0.5,0.5,0.5,0.5,0.5]
approach4_new = [1,0.6,0.4,0.2,0.2,0.2,0.2,0.2]
#approach1_x1 = [0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000]



ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 1.2)

#plt.yticks(range(0, 0.2, 1.2), fontsize=46)
#plt.xticks(range(0, 2, 14), fontsize=46)

#line, = plt.plot([1,5,2,4], '-')
#line.set_dashes([8, 4, 2, 4, 2, 4])

plt.plot(approach1_new, linestyle='--', dashes=dashList[4], linewidth=6, color='tomato', marker='s', markersize=18, label='Approach1')
plt.plot(approach2_new, linestyle='--', dashes=dashList[4], linewidth=6, color='royalblue', marker='^', markersize=18, label='Approach2')
plt.plot(approach3_new, linestyle='--', dashes=dashList[4], linewidth=6, color='gold', marker='*', markersize=18, label='Approach3')
plt.plot(approach4_new, linestyle='--', dashes=dashList[4], linewidth=6, color='orange', marker='d', markersize=18, label='Approach4')


plt.xlabel('# Pane to distributions', **csfont)
plt.ylabel('# of requests per min', **csfont)
#plt.legend(loc='upper left')
plt.legend(loc='upper right', fontsize=40, ncol=1, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
ax1.xaxis.grid(color='grey', linestyle='dashed')
ax1.yaxis.grid(color='grey', linestyle='dashed')
#plt.legend(shadow=True, loc=(0.01, 0.73),fontsize=30)

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
plt.savefig("./pareto_dist.pdf", bbox_inches='tight')
plt.show()

