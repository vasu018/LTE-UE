import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-paper')

matplotlib.rcParams.update({'font.size':40})
matplotlib.rcParams['figure.figsize'] = 14, 10

SMALL_SIZE = 55
MEDIUM_SIZE = 48
BIGGER_SIZE = 80

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize

f = plt.figure()
ax = f.add_subplot(111)

f.tight_layout()
f.subplots_adjust(left=0.12, right=0.99)

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
	plt.plot(bin_edges[0:-1], cdf, linestyle=ls, linewidth=8, label=Label)
	plt.ylim((0,1))
	plt.xlim((0, 120))
	plt.xticks([0, 20, 40, 60, 80, 100])
	plt.ylabel("CDF")
	plt.xlabel("Latency (ms)")
	plt.legend(loc='lower right')

attach_alone = []
service_alone = []
attach = []
service = []

p = open('actual/attach_10000_1.txt', 'r')
for i in p:
	i = i.strip().split(',')
	attach_alone = [float(j) for j in i if float(j)<65]
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

cdf(attach_alone, 'orange', 'Attach Alone', mk[0])
cdf(service_alone, 'magenta', 'Service Alone', mk[1])
cdf(attach, 'blue', 'Attach', mk[2])
cdf(service, 'maroon', 'Service', mk[3])
plt.grid(linestyle='--')
plt.savefig('Motivation_for_decomposition_1us_modified.pdf')
plt.show()
