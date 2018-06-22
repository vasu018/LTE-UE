import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
matplotlib.rcParams['figure.figsize'] = 20, 10

fig = plt.figure()
ax = fig.add_subplot(111)

fig.tight_layout()
fig.subplots_adjust(left=0.1, bottom=0.3, right=0.99)

def readXL(f, col):
    x = []
    workbook = xlrd.open_workbook(f)
    sheet = workbook.sheet_by_name('Sheet1')
    for value in sheet.col_values(col):
        if isinstance(value, float):
            x.append(value)
    return x

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
	plt.plot(bin_edges[0:-1], cdf,linestyle='--',linewidth=5, color=Colour, label=Label)
	plt.ylim((0,1))
	plt.ylabel("CDF")
	plt.xlabel("Latency (ms)")
	plt.legend(loc='lower right')

sf = []
sl = []
#f1 = open('service_10000_sf.txt', 'r')
#for i in f1: 
#    i = i.strip().split(',')
#    for j in i:
#        if (j):
#            sf.append(float(j))

#f1 = open('data_sf.txt', 'r')
#for i in f1: 
#    i = i.strip()
#    sf.append(float(i))

f2 = open('data_sl.txt', 'r')
for i in f2: 
    i = i.strip()
    sl.append(float(i))
    
print sl
print sf

#f2 = open('service_10000_sl.csv', 'r')
#for i in f2:
#    i = i.strip().split(',')
#    sl = [float(j) for j in i]

hv = readXL('TAUvsMig.xlsx', 1)
hv = [float(i) for i in hv if float(i)<=4800]

#cdf(sf, 'k', 'Normal Load')
cdf(sl, 'royalblue', 'Moderate Load')
cdf(hv, 'red', 'Overload')
plt.xscale('symlog')
plt.grid(linestyle='--')
plt.show()
