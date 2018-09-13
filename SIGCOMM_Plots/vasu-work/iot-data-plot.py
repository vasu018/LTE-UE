import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO
#import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

matplotlib.rcParams.update({'font.size':48})
matplotlib.rcParams['figure.figsize'] = 14, 8 

# Original Data
#RR+RR  25.75   17.89
#RR+Intra     23.7   6.92
#Inter+RR     9.25   12.35
#Inter+Intra        7.85   4.25

dataIn = StringIO(u"""     DeviceType     DataLoad      ControlLoad
1 Router 21023 7400
1 Cameras 20697 3106
1 Air_quality_sensors 448 373
1 Hubs 4169 1647
1 Computers 2631 716
1 Switches_&_Triggers 8911 5062
1 Electronics 905 1042
2 Cameras 22508 3164
2 Hubs 4152 1649
2 Router 22518 7438
2 Electronics 899 1030
2 Switches_&_Triggers 6301 3998
2 Computers 2110 673
2 Air_quality_sensors 446 366
2 Healthcare_devices 100 13
3 Router 37130 7933
3 Cameras 37781 3690
3 Switches_&_Triggers 6098 3902
3 Electronics 907 1048
3 Hubs 4287 1709
3 Computers 2402 664
3 Air_quality_sensors 522 382
4 Cameras 44927 4797
4 Router 155966 11033
4 Hubs 4567 1680
4 Switches_&_Triggers 8115 4349
4 Electronics 3515 1438
4 Computers 74795 7490
4 Air_quality_sensors 424 354
5 Router 74586 8406
5 Cameras 29159 3699
5 Electronics 1260 1105
5 Hubs 4582 1698
5 Air_quality_sensors 430 353
5 Computers 28410 2059
5 Switches_&_Triggers 9904 5250
5 Healthcare_devices 26 9
6 Router 18915 6643
6 Cameras 20697 3006
6 Switches_&_Triggers 6197 3876
6 Hubs 4245 1663
6 Electronics 892 1024
6 Computers 302 161
6 Air_quality_sensors 425 360
6 Healthcare_devices 75 13
""")

df = pd.read_csv(dataIn, index_col=0, delimiter=' ', skipinitialspace=True)

fig = plt.figure() # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

ind = np.arange(5)  # the x locations for the groups
width = 0.16

#rects2 = ax1.bar(ind+0.1, s2, width, color='lightgreen', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='50% Skew', hatch='/')
#df.DeviceType.plot(kind='bar', color='salmon', ax=ax, width=width, position=1)
#df.DataLoad.plot(kind='bar', color='royalblue', ax=ax2, width=width, position=0)

#df.DeviceType.plot(kind='bar', color='salmon', ax=ax,error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, label='Std. Dev of Load Dist. (%)', hatch='/', position=1, fontsize='50')
#df.DataLoad.plot(kind='bar', color='royalblue', ax=ax2, error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, label='SLO Violations (%)', hatch ='.', position=0,  fontsize='50')

df.DataLoad.plot(kind='bar', color='royalblue', ax=ax,error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, hatch='.', position=1+0.1, fontsize='32')
df.ControlLoad.plot(kind='bar', color='salmon', ax=ax2, error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, hatch ='/', position=0,  fontsize='32')

for tick in ax.get_xticklabels():
    tick.set_rotation(0)


#ax.set_xlabel('Hybrid LB Schemes')
#plt.xlabel('this is a xlabel\n(with newlines!)')
ax.set_ylabel('Std. Dev of Load Dist. (%)', fontsize='34')
ax2.set_ylabel('SLO Violations (%)', fontsize='34')
plt.xticks([0,1,2,3], ["RR +\nRR", "RR +\nOptimalNF", "SK-CH +\nRR", "SK-CH +\nOptimalNF"])

mar = mpatches.Patch(color='royalblue', label='Std. Dev of Load Dist', linewidth=2, hatch='.')
gre = mpatches.Patch(color='salmon', label='SLO Violations', hatch='/')
plt.legend(handles=[mar, gre], loc='upper right', fontsize=34, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
#plt.legend(handles=[mar, gre], loc='upper right', fontsize=42, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
#plt.legend(loc='upper right',ncol=1, fontsize=60, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
ax.set_ylim([0, 30])
ax.set_yticks(range(0, 30, 10))
ax2.set_ylim([0, 30])
ax2.set_yticks(range(0, 30, 10))
ax.xaxis.grid(color='gray',linestyle='--')
ax.yaxis.grid(color='gray', linestyle='--')
#ax2.xaxis.grid(color='gray',linestyle='--')
#ax2.yaxis.grid(color='gray', linestyle='--')
plt.savefig("./iot_data.pdf", bbox_inches='tight')

plt.show()
