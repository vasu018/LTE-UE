import xlrd
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':18})

f = plt.figure()

def readXL(f, col):
    x = []
    workbook = xlrd.open_workbook(f)
    sheet = workbook.sheet_by_name('Sheet1')
    for value in sheet.col_values(col):
        if isinstance(value, float):
            x.append(value)
        else:
            x.append(0)
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
	plt.plot(bin_edges[0:-1], cdf,linestyle='--', linewidth=5, color=Colour, label=Label)
	plt.ylim((0,1))
	plt.ylabel("CDF")
	plt.xlabel("Latency (ms)")
	plt.legend(loc='lower right')

sf = []
sl1 = []
sl2 = []

with open("./sf_failure_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        if x > 77 or x < 90:
            sf.append(float(y))

with open("./sl_host_failure_data.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        if x > 77 or x < 90:
            sl1.append(float(y))

with open("./sl_nf_failure_data_modified.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        if x > 77 or x < 90:
            sl2.append(float(y))


#sf = sf[int(len(sf)/1.2):]
#sl1 = sl1[int(len(sl1)/1.2):]
#sl2 = sl2[int(len(sl2)/1.2):]

cdf(sf, 'orange', 'Stateful Host Failure')
cdf(sl1, 'navy', 'Stateless Host Failure')
cdf(sl2, 'green', 'Stateless NF Failure')
plt.xscale('log')
plt.grid(linestyle='--')
plt.savefig("./cdf-ft.pdf", bbox_inches='tight')
plt.show()
