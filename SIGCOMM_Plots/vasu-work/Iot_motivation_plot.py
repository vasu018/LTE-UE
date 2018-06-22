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
sns.set_style('whitegrid')
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
#matplotlib.rcParams['figure.figsize'] = 3, 2

matplotlib.rcParams.update({'font.size':48})
matplotlib.rcParams['figure.figsize'] = 14, 8

#SMALL_SIZE = 40
#MEDIUM_SIZE = 40
#BIGGER_SIZE = 40

fig = plt.figure() 

ax = fig.add_subplot(111) 
ax2 = ax.twinx() 

#df = pd.read_csv('packet_count.txt', sep=' ')
df = pd.read_csv('graph.txt', sep=' ')
df.columns = ['Hour', 'Category', 'Data Packets', 'Control Packets']
df.sort_values(['Data Packets'], inplace=True)
df['Data Packets'] = df['Data Packets'].astype(int)
df['Category'] = df['Category'].str.replace('_',' ')
#print (df)
numHours = max(df['Hour'].values)
stack = [0] * (numHours + 1)
hour_list = range(1, numHours + 1)
width = 0.25
bars = []

pivot_df = df.pivot(index='Hour', columns='Category', values='Data Packets')
#pivot_df.sort_values(['Data Packets'], inplace=True)
pivot_df.sort_values(pivot_df.last_valid_index(), axis=1, inplace=True, ascending=False)
col_sequence = pivot_df.columns
pivot_df.plot.bar(stacked=True,ax=ax2,
                       colormap=ListedColormap(sns.color_palette("GnBu_d")),
                        ylim=[0, 300000],
                       rot=30,error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, position=0, fontsize='32')

ax.set_xticklabels(['12 - 4 am', '4 - 8 am', '8 am - 12 noon','12 noon - 4 pm', '4pm - 8 pm', '8 pm - 12 midnight'])

#plt.xticks(['12 - 4 am', '4 - 8 am', '8 am - 12 noon','12 noon - 4 pm', '4pm - 8 pm', '8 pm - 12 midnight'])
#plt.xticks(["12am - 4am", "4am - 8am", "8am - 12noon","12noon - 4pm", "4pm - 8pm", "8pm - 12midnight"])
ax2.set_xlabel('Hours of Day')
ax2.set_ylabel('Number of Data Packets')
#plt.savefig('Data.pdf')

pivot_df = df.pivot(index='Hour', columns='Category', values='Control Packets')
pivot_df = pivot_df[col_sequence]
pivot_df.plot.bar(stacked=True, ax=ax,
                       colormap=ListedColormap(sns.color_palette("GnBu_d")),
                       rot=30, ylim=[0, 50000], error_kw=dict(elinewidth=2,ecolor='k'), linewidth=2, width=width, capsize=10, position =1, fontsize='32')
#ax.set_xticklabels(['12 - 4 am', '4 - 8 am', '8 am - 12 noon',  '12 noon - 4 pm', '4pm - 8 pm', '8 pm - 12 midnight'])
ax.set_xlabel('Hours of Day')
ax.set_ylabel('Number of Control Packets')
plt.savefig('Iot_motivation_plot.pdf')
plt.show()
