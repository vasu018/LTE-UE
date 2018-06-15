import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':60})
matplotlib.rcParams['figure.figsize'] = 14, 10

#pepc = [25.6, 14.4, 11.86, 9.2, 8]
ch = [21.8, 9.4, 4.86, 3.2, 2.1]
rr = [19.7, 7.6, 4.35, 3.81, 1.8]
skch = [2.75, 2.1, 1.15, 0.95, 0.4]
#ilp = [1.39, 1, 1, 0.81, 0.37]
#maglev = [16.3, 8.2, 3.2, 2.81, 1.6]
hs = [3, 4, 5, 6, 7]
dashList = [(5,2),(2,5),(4,10),(3,3,2,2),(5,5,20,5)]

fig, ax1 = plt.subplots()
line, = plt.plot([1,5,2,4], '-')
line.set_dashes([8, 4, 2, 4, 2, 4])


#plt.plot(hs, pepc, marker='p', color='red', linewidth=5, markersize=18, linestyle='--', label='PEPC')

plt.plot(hs, rr, marker='o', color='tomato', linewidth=5, markersize=18, linestyle='--', label='RR')
plt.plot(hs, ch, marker='D', color='gold', linewidth=5, markersize=18, linestyle='--', label='CH')
plt.plot(hs, skch, marker='^', color='royalblue', linewidth=5, markersize=18, linestyle='--', label='SK-CH')


#plt.plot(hs, ilp, marker='s', color='salmon', linewidth=5, markersize=18, linestyle='--', label='ILP')
#plt.plot(hs, maglev, marker='*', color='green', linewidth=5, markersize=18, linestyle='--', label='Maglev')

plt.xlabel('Average Latency')
plt.ylabel('Traffic type')
plt.legend(loc='upper right', fontsize=50, ncol=2, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
ax1.xaxis.grid(color='grey', linestyle='dashed')
ax1.yaxis.grid(color='grey', linestyle='dashed')

#plt.xticks(hs, ['3', '4', '5', '6', '7'])
plt.grid(linestyle='--')
plt.xlim([2.9, 7.1])
plt.xticks(range(3, 8, 1))
plt.ylim([0, 30])
plt.yticks(range(0, 30, 5))
plt.savefig("./avg-latency.pdf", bbox_inches='tight')
plt.show()
