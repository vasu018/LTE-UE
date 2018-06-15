import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import itertools
from collections import OrderedDict
from functools import partial

csfont = {'fontname':'Comic Sans MS', 'fontsize':'52'}
csfont2 = {'fontname':'Comic Sans MS', 'fontsize':'36'}
hfont = {'fontname':'Helvetica', 'fontsize':'24'}
dashList = [(5,2),(2,5),(4,10),(3,3,2,2),(5,5,20,5)]

matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 9, 10


fig, ax = plt.subplots()
fig.tight_layout()
fig.subplots_adjust(left=0.12, right=0.99)
#ax = fig.add_subplot(111)
#plt.legend(loc=4, prop={'size': 6})
#plt.legend(fontsize=16)
#ax.legend(handletextpad=0.1)

N = 1 
orig = [195276]
bitseg = [57935]
alpaca = [62972]
approach1 = [45695]
approach2 = [67987]

params = {'legend.fontsize': 38,
          'legend.handlelength': 2,
          'legend.ncols':2}
plt.rcParams.update(params)



#orig = matplotlib.pyplot.gca()
#mkfunc = lambda orig, pos: '%1.1fM' % (orig * 1e-6) if orig >= 1e6 else '%1.1fK' % (orig * 1e-3) if orig >= 1e3 else '%1.1f' % orig
#mkformatter = matplotlib.ticker.FuncFormatter(mkfunc)
#orig.xaxis.set_major_formatter(mkformatter)

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.18                      # the width of the bars


#hatch_cycle = cycler('hatch', ['/', '*', '+', '|'])

## the bars
rects1 = ax.bar(ind, orig, width,
                color='maroon',
#                yerr=menStd,
                error_kw=dict(elinewidth=0,ecolor='maroon'))

rects2 = ax.bar(ind+width, bitseg, width,
                    color='gold',
#                    yerr=womenStd,
                    error_kw=dict(elinewidth=2,ecolor='gold'))

rects3 = ax.bar(ind+2*width, alpaca, width,
                    color='cyan',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='cyan'))

rects4 = ax.bar(ind+3*width, approach1, width,
                    color='magenta',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='magenta'))

rects5 = ax.bar(ind+4*width, approach2, width,
                    color='blue',
#                    yerr=animalStd,
                    error_kw=dict(elinewidth=2,ecolor='blue'))

# axes and labels
ax.set_xlim(-width,len(ind)+0.12)
ax.set_ylim(0,200000)
#ax.set_ylabel('')
#ax.set_yscale('symlog')
plt.ylabel('# Rules', **csfont)
plt.xlabel('Rule placement with 3 Datasets', **csfont)

#ax.set_title('Tag assignment')
#xTickMarks = ['SDMZ Campus Net'+str(i) for i in range(1,6)]
xTickMarks = ['SDMZ Campus \nNet 1', 'SDMZ Campus \nNet 2', 'Synthesized \nCampus 1']
#xTickMarks = ['SDMZ Campus 1', 'SDMZ Campus 2', 'Synthesized Campus 1']
ax.set_xticks(ind+0.50)
xtickNames = ax.set_xticklabels(xTickMarks, **csfont2)
#plt.setp(xtickNames, rotation=45, fontsize=10)
#plt.setp(xtickNames, fontsize=10)


#ax = matplotlib.pyplot.gca()
#mkfunc = lambda x2, pos: '%1.1fM' % (x2 * 1e-6) if x2 >= 1e6 else '%1.1fK' % (x2 * 1e-3) if x2 >= 1e3 else '%1.1f' % x2
#        mkformatter = matplotlib.ticker.FuncFormatter(mkfunc)
#        x2.xaxis.set_major_formatter(mkformatter)

## add a legend
plt.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('Original', 'Bit Segmentation', 'Alpaca', 'Approach1', 'Approach2'))

##plt.legend( (rects2[0], rects3[0], rects4[0], rects5[0]), ('Bit Segmentation', 'Alpaca', 'Approach1', 'Approach2'))
#plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, ncols=2, loc=2)

#locs = ["upper left", "lower left", "center right"]
plt.legend(loc='upper left')
plt.legend(shadow=True, loc=(0.01, 0.78))
#plt.legend(ncols=3)

ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
plt.savefig("./rule-efficiency2.pdf", bbox_inches='tight')
plt.show()
