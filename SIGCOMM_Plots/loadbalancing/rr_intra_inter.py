import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO
#import numpy as np
import matplotlib
#import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

matplotlib.rcParams.update({'font.size':52})
matplotlib.rcParams['figure.figsize'] = 14, 10

# Original Data
#RR+RR  25.75   17.89
#RR+Intra     23.7   6.92
#Inter+RR     9.25   12.35
#Inter+Intra        7.85   4.25

dataIn = StringIO(u"""     SDResource     SLOViolation
RR+RR  18.65   21.89
RR+ViableNF     16.65   9.92
SK-CH+RR     5.32   16.35
SK-CH+ViableNF  2.85   4.25
""")

df = pd.read_csv(dataIn, index_col=0, delimiter=' ', skipinitialspace=True)

fig = plt.figure() # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

ind = np.arange(5)  # the x locations for the groups
width = 0.25

#rects2 = ax1.bar(ind+0.1, s2, width, color='lightgreen', error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, capsize=10, label='50% Skew', hatch='/')
#df.SDResource.plot(kind='bar', color='salmon', ax=ax, width=width, position=1)
#df.SLOViolation.plot(kind='bar', color='royalblue', ax=ax2, width=width, position=0)

#df.SDResource.plot(kind='bar', color='salmon', ax=ax,error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, label='Std. Dev of Load Dist. (%)', hatch='/', position=1, fontsize='50')
#df.SLOViolation.plot(kind='bar', color='royalblue', ax=ax2, error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, label='SLO Violations (%)', hatch ='.', position=0,  fontsize='50')

df.SDResource.plot(kind='bar', color='salmon', ax=ax,error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, hatch='.', position=1+0.1, fontsize='50')
df.SLOViolation.plot(kind='bar', color='royalblue', ax=ax2, error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, hatch ='/', position=0,  fontsize='50')
for tick in ax.get_xticklabels():
    tick.set_rotation(20)

ax.set_ylabel('Std. Dev of Load Dist. (%)', fontsize='50')
ax2.set_ylabel('SLO Violations (%)', fontsize='50')

mar = mpatches.Patch(color='salmon', label='Std. Dev of Load Dist', linewidth=2, hatch='.')
gre = mpatches.Patch(color='royalblue', label='SLO Violations', hatch='/')
plt.legend(handles=[mar, gre], loc='upper right', fontsize=46, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
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
plt.savefig("./inter-intra.pdf", bbox_inches='tight')

plt.show()
