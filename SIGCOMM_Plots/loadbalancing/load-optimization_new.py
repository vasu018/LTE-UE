import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import itertools
from collections import OrderedDict
from functools import partial
from matplotlib import gridspec

hfont = {'fontname':'Helvetica', 'fontsize':'48'}
dashList = [(5,2),(2,5),(4,10),(3,3,2,2),(5,5,20,5)]

matplotlib.rcParams.update({'font.size':48})
matplotlib.rcParams['figure.figsize'] = 14, 10

fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.subplots_adjust(left=0.07, right=0.99)

N1 = 4 
rr = [6.2, 5.3, 3.6, 6.7]
ch = [6.7,6.2,4.7,7]
maglev = [6.3, 5.6, 3.8, 6.8]
sk_ch = [4.1,3.2,2.9,4.2]

N2 = 1 
rr_sim = [89]
ch_sim = [97]
maglev_sim = [83]
sk_ch_sim = [53]

## necessary variables
ind1 = np.arange(N1)                # the x locations for the groups
width1 = 0.22                      # the width of the bars

ind2 = np.arange(N2)                # the x locations for the groups
width2 = 0.10                      # the width of the bars


## the bars
rects1 = ax1.bar(ind1, rr, width1,
                color='firebrick',
#                yerr=menStd,
                error_kw=dict(elinewidth=0,ecolor='firebrick'), hatch = '|')

rects2 = ax1.bar(ind1+width1, ch, width1,
                    color='gold',
#                    yerr=womenStd,
                    error_kw=dict(elinewidth=2,ecolor='gold'), hatch='/')

rects3 = ax1.bar(ind1+2*width1, maglev, width1,
                    color='lightpink',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='lightpink'), hatch='.')

rects4 = ax1.bar(ind1+3*width1, sk_ch, width1,
                    color='lightgreen',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='lightgreen'), hatch='-')

#rects5 = ax1.bar(ind1+5*width1, approach2_1, width1,
#                    color='royalblue',
##                    yerr=animalStd,
#                    error_kw=dict(elinewidth=2,ecolor='royalblue'), hatch='+')



## the bars
rects6 = ax2.bar(ind2-0.05, rr_sim, width2,
                color='firebrick',
#                yerr=menStd,
                error_kw=dict(elinewidth=0,ecolor='firebrick'),label='RR', hatch='|')

rects7 = ax2.bar(ind2+width2-0.05, ch_sim, width2,
                    color='gold',
#                    yerr=womenStd,
                    error_kw=dict(elinewidth=2,ecolor='gold'),label='CH', hatch='/')

rects8 = ax2.bar(ind2+2*width2-0.05, maglev_sim, width2,
                    color='lightpink',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='lightpink'),label='Maglev', hatch='.')

rects9 = ax2.bar(ind2+3*width2-0.05, sk_ch_sim, width2,
                    color='lightgreen',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='lightgreen'),label='SK-CH', hatch='-')



def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()

        # Fraction of axis height taken up by this rectangle
        p_height = (height / y_height)

        # If we can fit the label above the column, do that;
        # otherwise, put it inside the column.
        if p_height > 0.95: # arbitrary; 95% looked good to me.
            label_position = height - (y_height * 0.05)
        else:
            label_position = height + (y_height * 0.01)

        ax.text(rect.get_x() + rect.get_width()/2., label_position,
                '%d' % int(height),
                ha='center', va='bottom',**hfont)					
					
#ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
#          ncol=3, fancybox=True, shadow=True)

# axes and labels
plt.subplot(121)
ax1.set_xlim(-width1-0.05,len(ind1)+width1)
ax1.set_ylim(0,10)
plt.ylabel('# Servers', **hfont)
xTickMarks = ['T1', 'T2', 'T3', 'T4']
ax1.set_xticks(ind1+0.50)
xtickNames = ax1.set_xticklabels(xTickMarks, **hfont)
ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
vals1 = ax1.get_yticks()
plt.legend(loc='upper left',fontsize=26,handleheight=2)

plt.subplot(121)
ax2.set_xlim(-2*width2-0.1,len(ind2))
ax2.set_ylim(0,110)
xTickMarks = ['T4 (Simulated\nSetup)']
ax2.set_xticks(ind2+0.35)
xtickNames = ax2.set_xticklabels(xTickMarks, **hfont)
ax2.set_axisbelow(True)
ax2.yaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
vals = ax2.get_yticks()
#ax2.set_yticklabels([str(x/1000) +  "k" for x in vals])
ax2.legend(loc='upper right',fontsize=26,handleheight=2)
plt.xlabel('Traffic Distributions', **hfont)

#plt.legend(loc='upper left')
#plt.legend(shadow=True, loc=(0.01, 0.78))
#plt.subplots_adjust(left=0.12, wspace=0.99, top=0.99)
plt.savefig("./load_optimization_new.pdf", bbox_inches='tight')
plt.show()
