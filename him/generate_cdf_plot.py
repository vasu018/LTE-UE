import numpy as np
import sys
import matplotlib.pyplot as plt

f = plt.figure()
def cdf80(data, Colour, Label, outfile):
    global f
    data_size=len(data)
    # trim the data in order to magnify
    data=data[data<40]
    # Set bins edges
    data_set=sorted(set(data))
    bins=np.append(data_set, data_set[-1]+1)
    print (bins)

    # Use the histogram function to bin the data
    count = 0
    for i in data:
        count += 1
        if np.isnan(i):
            print (count)
    counts, bin_edges = np.histogram(data, bins=bins, density=False)
    counts=counts.astype(float)/data_size

    # Find the cdf
    cdf = np.cumsum(counts)

    # Plot the cdf
    plt.plot(bin_edges[0:-1], cdf,linestyle='--', color=Colour, label=Label)
    plt.ylim((0,0.8))
    plt.ylabel("CDF")
    plt.xlabel("Latency (ms)")
    #plt.grid(True)
    plt.legend(loc='lower right')
    f.savefig(outfile)

def cdf(data, Colour, Label, outfile):
    global f
    data_size=len(data)

    # Set bins edges
    data_set=sorted(set(data))
    bins=np.append(data_set, data_set[-1]+1)
    print (bins)

    # Use the histogram function to bin the data
    count = 0
    for i in data:
        count += 1
        if np.isnan(i):
            print (count)
    counts, bin_edges = np.histogram(data, bins=bins, density=False)
    counts=counts.astype(float)/data_size

    # Find the cdf
    cdf = np.cumsum(counts)

    # Plot the cdf
    plt.plot(bin_edges[0:-1], cdf,linestyle='--', color=Colour, label=Label)
    plt.ylim((0,1))
    plt.ylabel("CDF")
    plt.xlabel("Latency (ms)")
    #plt.grid(True)
    plt.legend(loc='lower right')
    f.savefig(outfile)



if (len(sys.argv) < 4):
	print ("Usage : python3 generate_cdf_plot.py graph_desc file1_desc filename1.csv file2_desc filename2.csv output_graph_name")
	exit()

graph_desc = sys.argv[1]
file1_desc = sys.argv[2]
file1 = sys.argv[3]

file2_desc = sys.argv[4]
file2 = sys.argv[5]
outfile = sys.argv[6]

data1 = np.genfromtxt(file1, delimiter=',')
data2 = np.genfromtxt(file2, delimiter=',')

# remove 0s from data
data1 = data1[data1 != 0]
data2 = data2[data2 != 0]

cdf(data1[:-2], 'b', file1_desc, outfile)
cdf(data2[:-2], 'r', file2_desc, outfile)
#cdf80(data1[:-2], 'b', file1_desc, outfile)
#cdf80(data2[:-2], 'r', file2_desc, outfile)
plt.title(graph_desc)
plt.show()

