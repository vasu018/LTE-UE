import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO
import matplotlib
import matplotlib.patches as mpatches
import seaborn as sns
import matplotlib as mlt
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
sns.set()
sns.set_style('ticks')
from matplotlib import rcParams
#rcParams.update({'figure.autolayout': True})
#matplotlib.rcParams['figure.figsize'] = 3, 2

matplotlib.rcParams.update({'font.size':48})
matplotlib.rcParams['figure.figsize'] = 16,8 

#SMALL_SIZE = 40
#MEDIUM_SIZE = 40
#BIGGER_SIZE = 40

fig = plt.figure() 

ax = fig.add_subplot(111) 
ax2 = ax.twinx() 
fig.subplots_adjust(left=0.12, bottom=0.17, right=0.88)
1
df = pd.read_csv('packet_count_new.txt', sep=' ')
#df = pd.read_csv('graph.txt', sep=' ')
df.columns = ['Hour', 'Category', 'DataPackets', 'Control Packets']
df.sort_values(['DataPackets'], inplace=True)
df['DataPackets'] = df['DataPackets'].astype(int) / 250000
df['Control Packets'] = df['Control Packets'].astype(int) / 30000
#df['Category'] = df['Category'].str.replace('_',' ')
#print (df)
numHours = max(df['Hour'].values)
stack = [0] * (numHours + 1)
hour_list = range(1, numHours + 1)
width = 0.25
bars = []

pivot_df = df.pivot(index='Hour', columns='Category', values='DataPackets')
#pivot_df.sort_values(['DataPackets'], inplace=True)
pivot_df.sort_values(pivot_df.last_valid_index(), axis=1, inplace=True, ascending=False)
# sns.palplot(sns.color_palette("Set1", n_colors=8, desat=.5))
col_sequence = pivot_df.columns
pivot_df.plot.bar(stacked=True,ax=ax,
                       colormap=ListedColormap(sns.color_palette("Set1",n_colors=8, desat=.5)),
                       #colormap=ListedColormap(sns.color_palette("RdBu")),
                        ylim=[0, 1],
                       rot=30,error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, position=0, fontsize='32')

#ax.set_xticklabels(['12am - 4am', '4am - 8am', '8am - 12pm','12pm - 4pm', '4pm - 8pm', '8pm - 12am'],fontsize = '22',rotation ='0')

#plt.xticks(['12 - 4 am', '4 - 8 am', '8 am - 12 noon','12 noon - 4 pm', '4pm - 8 pm', '8 pm - 12 midnight'])
#plt.xticks(["12am - 4am", "4am - 8am", "8am - 12noon","12noon - 4pm", "4pm - 8pm", "8pm - 12midnight"])
ax2.set_xlabel('Hours of Day', fontsize = '42')
ax2.set_ylabel('Normalized DataLoad', fontsize='42')
#ax.set_yticks(fontsize='36')
#plt.savefig('Data.pdf')

pivot_df2 = df.pivot(index='Hour', columns='Category', values='Control Packets')
pivot_df2.sort_values(pivot_df2.last_valid_index(), axis=1, inplace=True, ascending=False)
pivot_df2 = pivot_df2[col_sequence]
pivot_df2.plot.bar(stacked=True, ax=ax2,
                       #colormap=ListedColormap(sns.color_palette("RdBu")),
                       colormap=ListedColormap(sns.color_palette("Set1",n_colors=8, desat=.5)),
                       #colormap=ListedColormap(sns.color_palette("muted")),
                       rot=30, ylim=[0, 1], error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, position =1, fontsize='32')
ax.legend().set_visible(False)
ax.set_xticklabels(['Data  Ctrl\n 12am - 4am', 'Data  Ctrl\n 4am - 8am', 'Data  Ctrl\n 8am - 12pm',  'Data  Ctrl\n 12pm - 4pm', 'Data  Ctrl\n 4pm - 8pm', 'Data  Ctrl\n 8pm - 12am'],fontsize = '22',rotation ='0')
ax.set_xlabel('Hours of Day', fontsize='42')
ax.set_ylabel('Normalized Control Load', fontsize='42')
plt.legend(loc='upper left',ncol=3, fontsize=22, borderpad=None, borderaxespad=None,fancybox=True, framealpha=0.5)
ax.set_axisbelow(True)
#ax.yaxis.grid(color='gray', linestyle='dashed')
#ax.xaxis.grid(color='gray', linestyle='dashed')
ax2.set_axisbelow(True)
ax2.yaxis.grid(color='gray', linestyle='dashed')
ax2.xaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
#ax.set_yticks(fontsize='36')
plt.savefig('Iot_motivation_plot.pdf')
plt.show()
