import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10

f = plt.figure()

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
	plt.plot(bin_edges[0:-1], cdf, linestyle=ls, linewidth=5, color=Colour, label=Label)
	plt.ylim((0,1))
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

#mk = ['o', 'x', '*', '+']
mk = ['--', ':', '-', '-.']

cdf(attach_alone, 'orange', 'Attach Alone', mk[0])
cdf(service_alone, 'navy', 'Service Alone', mk[1])
cdf(attach, 'm', 'Attach', mk[2])
cdf(service, 'k', 'Service', mk[3])
plt.savefig('Motivation_for_decomposition_1us_modified.pdf')

plt.grid(linestyle='--')
plt.show()
