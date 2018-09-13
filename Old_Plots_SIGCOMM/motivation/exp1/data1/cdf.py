import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})

f = plt.figure()

def cdf(data, Colour, Label):
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
	plt.plot(bin_edges[0:-1], cdf,linestyle='--', color=Colour, label=Label)
	plt.ylim((0,1))
	plt.ylabel("CDF")
	plt.xlabel("Latency (ms)")
	plt.legend(loc='lower right')

attach_alone = []
service_alone = []
attach = []
service = []

p = open('attach_10000_1.csv', 'r')
for i in p:
	i = i.strip().split(',')
	attach_alone = [float(j) for j in i]
p = open('service_10000_1.csv', 'r')
for i in p:
        i = i.strip().split(',')
        service_alone = [float(j) for j in i]
p = open('attach_5000_1.csv', 'r')
for i in p:
	i = i.strip().split(',')
        print i
	attach = [float(j) for j in i]
p = open('service_5000_1.csv', 'r')
for i in p:
        i = i.strip().split(',')
        service = [float(j) for j in i]

cdf(attach_alone, 'r', 'Attach Alone')
cdf(service_alone, 'b', 'Service Alone')
cdf(attach, 'g', 'Attach')
cdf(service, 'k', 'Service')

plt.show()
