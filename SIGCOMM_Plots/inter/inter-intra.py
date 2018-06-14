import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import itertools
from collections import OrderedDict
from functools import partial

#csfont = {'fontname':'Comic Sans MS', 'fontsize':'52'}
#csfont2 = {'fontname':'Comic Sans MS', 'fontsize':'42'}

#csfont3 = {'fontname':'Comic Sans MS', 'fontsize':'52'}

hfont = {'fontname':'Helvetica', 'fontsize':'24'}
dashList = [(5,2),(2,5),(4,10),(3,3,2,2),(5,5,20,5)]

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 14, 10


fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.tight_layout()
fig.subplots_adjust(left=0.10, right=0.99)


#params = {'legend.fontsize': 28,
#          'legend.handlelength': 2,
#          'legend.ncols':2}
#plt.rcParams.update(params)

N1 = 2 
orig_1 = [7987, 5325]
#bitseg_1 = [3257, 2137]
bitseg_1 = [4257, 3137]
alpaca_1 = [4497, 3358]
approach1_1 = [1997, 1635]
approach2_1 = [2495, 1987]

#N1 = 2 
#orig_1 = [8987, 6325]
#bitseg_1 = [3257, 2137]
#alpaca_1 = [3497, 2358]
#approach1_1 = [2197, 1435]
#approach2_1 = [3695, 2487]

N2 = 1 
orig_2 = [137276]
bitseg_2 = [74935]
alpaca_2 = [75972]
approach1_2 = [38695]
approach2_2 = [46987]

#N2 = 1 
#orig_2 = [142276]
#bitseg_2 = [57935]
#alpaca_2 = [62972]
#approach1_2 = [45695]
#approach2_2 = [67987]

## necessary variables
ind1 = np.arange(N1)                # the x locations for the groups
width1 = 0.18                      # the width of the bars

ind2 = np.arange(N2)                # the x locations for the groups
width2 = 0.12                      # the width of the bars


#hatch_cycle = cycler('hatch', ['/', '*', '+', '|'])

## the bars
rects1 = ax1.bar(ind1+width1, orig_1, width1,
                color='firebrick',
#                yerr=menStd,
                error_kw=dict(elinewidth=0,ecolor='firebrick'))

rects2 = ax1.bar(ind1+2*width1, bitseg_1, width1,
                    color='gold',
#                    yerr=womenStd,
                    error_kw=dict(elinewidth=2,ecolor='gold'), hatch='/')

rects3 = ax1.bar(ind1+3*width1, alpaca_1, width1,
                    color='lightpink',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='lightpink'), hatch='.')

rects4 = ax1.bar(ind1+4*width1, approach1_1, width1,
                    color='lightgreen',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='lightgreen'), hatch='-')

rects5 = ax1.bar(ind1+5*width1, approach2_1, width1,
                    color='royalblue',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='royalblue'), hatch='+')



## the bars
rects6 = ax2.bar(ind2-0.05, orig_2, width2,
                color='firebrick',
#                yerr=menStd,
                error_kw=dict(elinewidth=0,ecolor='firebrick'),label='Original')

rects7 = ax2.bar(ind2+width2-0.05, bitseg_2, width2,
                    color='gold',
#                    yerr=womenStd,
                    error_kw=dict(elinewidth=2,ecolor='gold'),label='Bit Seg', hatch='/')

rects8 = ax2.bar(ind2+2*width2-0.05, alpaca_2, width2,
                    color='lightpink',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='lightpink'),label='Alpaca', hatch='.')

rects9 = ax2.bar(ind2+3*width2-0.05, approach1_2, width2,
                    color='lightgreen',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='lightgreen'),label='Approach1', hatch='-')

rects10 = ax2.bar(ind2+4*width2-0.05, approach2_2, width2,
                    color='royalblue',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='royalblue'),label='Approach2', hatch='+')



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
ax1.set_ylim(0,8500)
plt.ylabel('# Rules', **hfont)
xTickMarks = ['Campus \nNet 1', 'Campus \nNet 2']
#xTickMarks = ['Campus \nNet 1', 'Campus \nNet 2']
ax1.set_xticks(ind1+0.50)
xtickNames = ax1.set_xticklabels(xTickMarks, **hfont)
ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
vals1 = ax1.get_yticks()
#vals1.yticks(range(0, 8500, 2000), fontsize=46)
ax1.set_yticklabels([str(x/1000) +  "k" for x in vals1])

plt.subplot(121)
#ax2.set_xlim(-width2,len(ind2))
#ax2.yticks(range(0, 170000, 40000), fontsize=46)
ax2.set_xlim(-2*width2-0.1,len(ind2))
ax2.set_ylim(0,170000)
#plt.ylabel('# Rules', **csfont)
#plt.xlabel('Rule placement with 3 Datasets', **csfont)
xTickMarks = ['Synthesized \nCampus Net 1']
#xTickMarks = ['Syn. \nCamp 1']
ax2.set_xticks(ind2+0.35)
xtickNames = ax2.set_xticklabels(xTickMarks, **hfont)
ax2.set_axisbelow(True)
ax2.yaxis.grid(color='gray', linestyle='dashed')
#plt.xlabel('Rule Space Optimization', **csfont)
plt.grid(linestyle='--')
vals = ax2.get_yticks()
ax2.set_yticklabels([str(x/1000) +  "k" for x in vals])
ax2.legend(loc='upper right',fontsize=28,handleheight=2)

#plt.legend(loc='upper left')
#plt.legend(shadow=True, loc=(0.01, 0.78))
#plt.subplots_adjust(left=0.12, wspace=0.99, top=0.99)
plt.savefig("./interandintra.pdf", bbox_inches='tight')
plt.show()
