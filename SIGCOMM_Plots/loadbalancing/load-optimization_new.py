import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import itertools
from collections import OrderedDict
from functools import partial

csfont = {'fontname':'Comic Sans MS', 'fontsize':'52'}
csfont2 = {'fontname':'Comic Sans MS', 'fontsize':'42'}

csfont3 = {'fontname':'Comic Sans MS', 'fontsize':'52'}

hfont = {'fontname':'Helvetica', 'fontsize':'24'}
dashList = [(5,2),(2,5),(4,10),(3,3,2,2),(5,5,20,5)]

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14, 10


fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.tight_layout()
fig.subplots_adjust(left=0.07, right=0.99)


#params = {'legend.fontsize': 28,
#          'legend.handlelength': 2,
#          'legend.ncols':2}
#plt.rcParams.update(params)

N1 = 4 
rr = [6.2, 5.3, 3.6, 6.7]
ch = [6.7,6.2,4.7,7]
maglev = [6.3, 5.6, 3.8, 6.8]
sk_ch = [4.1,3.2,2.9,4.2]

N2 = 1 
rr_sim = [89]
ch_sim = [97]
maglev_sim = [83]
sk_ch_sim = [57]

## necessary variables
ind1 = np.arange(N1)                # the x locations for the groups
width1 = 0.18                      # the width of the bars

ind2 = np.arange(N2)                # the x locations for the groups
width2 = 0.12                      # the width of the bars


#hatch_cycle = cycler('hatch', ['/', '*', '+', '|'])

## the bars
rects1 = ax1.bar(ind1+width1, rr, width1,
                color='firebrick',
#                yerr=menStd,
                error_kw=dict(elinewidth=0,ecolor='firebrick'), hatch = '|')

rects2 = ax1.bar(ind1+2*width1, ch, width1,
                    color='gold',
#                    yerr=womenStd,
                    error_kw=dict(elinewidth=2,ecolor='gold'), hatch='/')

rects3 = ax1.bar(ind1+3*width1, maglev, width1,
                    color='lightpink',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='lightpink'), hatch='.')

rects4 = ax1.bar(ind1+4*width1, sk_ch, width1,
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
                ha='center', va='bottom',**csfont3)					
					
#autolabel(rects6,ax2)
#autolabel(rects7, ax2)
#autolabel(rects8, ax2)
#autolabel(rects9, ax2)
#autolabel(rects10, ax2)

ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

# Shrink current axis by 20%
#box = ax.get_position()
#ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# axes and labels
plt.subplot(121)
ax1.set_xlim(-width1-0.05,len(ind1)+width1)
ax1.set_ylim(0,10)
plt.ylabel('# Servers', **csfont)
xTickMarks = ['T1', 'T2', 'T3', 'T4']
#xTickMarks = ['Campus \nNet 1', 'Campus \nNet 2']
ax1.set_xticks(ind1+0.50)
xtickNames = ax1.set_xticklabels(xTickMarks, **csfont2)
ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
vals1 = ax1.get_yticks()
#vals1.yticks(range(0, 8500, 2000), fontsize=46)
#ax1.set_yticklabels([str(x/1000) +  "k" for x in vals1])

plt.subplot(121)
#ax2.set_xlim(-width2,len(ind2))
#ax2.yticks(range(0, 170000, 40000), fontsize=46)
ax2.set_xlim(-2*width2-0.1,len(ind2))
ax2.set_ylim(0,110)
#plt.ylabel('# Rules', **csfont)
#plt.xlabel('Rule placement with 3 Datasets', **csfont)
xTickMarks = ['Synthesized \n IoT Traffic']
#xTickMarks = ['Syn. \nCamp 1']
ax2.set_xticks(ind2+0.35)
xtickNames = ax2.set_xticklabels(xTickMarks, **csfont2)
ax2.set_axisbelow(True)
ax2.yaxis.grid(color='gray', linestyle='dashed')
#plt.xlabel('Rule Space Optimization', **csfont)
plt.grid(linestyle='--')
vals = ax2.get_yticks()
#ax2.set_yticklabels([str(x/1000) +  "k" for x in vals])
ax2.legend(loc='upper right',fontsize=28,handleheight=2)

#plt.legend(loc='upper left')
#plt.legend(shadow=True, loc=(0.01, 0.78))
#plt.subplots_adjust(left=0.12, wspace=0.99, top=0.99)
plt.savefig("./load_optimization_new.pdf", bbox_inches='tight')
plt.show()
