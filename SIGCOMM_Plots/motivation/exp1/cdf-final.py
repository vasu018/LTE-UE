import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':40})
matplotlib.rcParams['figure.figsize'] = 14, 10
import random

csfont = {'fontname':'Comic Sans MS', 'fontsize':'52'}
csfont2 = {'fontname':'Comic Sans MS', 'fontsize':'46'}
hfont = {'fontname':'Helvetica', 'fontsize':'80'}

f = plt.figure()
ax = f.add_subplot(111)

f.tight_layout()
f.subplots_adjust(left=0.14, right=0.99, bottom=0.15)

def cdf(data, Colour, Label, ls):
	global f
	data_size=len(data)
	
	# Set bins edges
	data_set=sorted(set(data))
	bins=np.append(data_set, data_set[-1]+1)
	
	# Use the histogram function to bin the data
	counts, bin_edges = np.histogram(data, bins=bins, density=False)
	
	counts=counts.astype(float)/data_size
	
	# Find the cdf
	cdf = np.cumsum(counts)
	
	# Plot the cdf
	plt.plot(bin_edges[0:-1], cdf, linestyle=ls, linewidth=6, color=Colour, label=Label)
	plt.ylim((0,1))
	plt.ylabel("CDF", **hfont)
	plt.xlabel("Latency (ms)", **hfont)
	plt.legend(loc='lower right')
    #plt.legend(shadow=True, loc=(0.01, 0.73), fontsize=46)

attach_alone = []
service_alone = []
attach = []
service = []

p = open('actual/attach_10000_1.txt', 'r')
for i in p:
	i = i.strip().split(',')
	#attach_alone = [float(j) for j in i if float(j)<65]
	attach_alone = [float(j) for j in i if float(j)<63]

p = open('actual/service_10000_1.txt', 'r')
for i in p:
        i = i.strip().split(',')
        service_alone = [float(j)+random.random() for j in i]

p = open('actual/attach_5000_1.txt', 'r')
for i in p:
	i = i.strip().split(',')
	attach = [float(j) for j in i]

p = open('actual/service_5000_1.txt', 'r')
for i in p:
        i = i.strip().split(',')
        service = [float(j) for j in i]

mk = ['-', '--', '-.', ':']

cdf(attach_alone, 'royalblue', 'Attach Alone', '-')
cdf(service_alone, 'tomato', 'Service Alone', '-')
cdf(attach, 'green', 'Attach', '--')
cdf(service, 'maroon', 'Service', '--')
plt.xlim((0,110))
plt.yticks(fontsize=46)
plt.xticks(range(0, 110, 20), fontsize=46)


ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
plt.grid(linestyle='--')
plt.savefig('Motivation_for_decomposition_1us_modified.pdf')
plt.show()
