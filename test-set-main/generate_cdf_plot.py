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

def cdf(data, Label, outfile):
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
    plt.plot(bin_edges[0:-1], cdf,linestyle='--', label=Label)
    plt.ylim((0,1))
    plt.ylabel("CDF")
    plt.xlabel("Latency (ms)")
    #plt.grid(True)
    plt.legend(loc='lower right')
    f.savefig(outfile)



if (len(sys.argv) < 4):
	print ("Usage : python3 generate_cdf_plot.py graph_desc no_of_files file1_desc filename1.csv [file2_desc filename2.csv] ....  output_graph_name")
	exit()
file_desc = []
filename = []
data = []

graph_desc = sys.argv[1]
plt.title(graph_desc)

no_files = int(sys.argv[2])

for i in range(0, no_files):
    file_desc.append(sys.argv[2 + (i*2 + 1)])
    filename.append(sys.argv[2 + (i*2 + 2)])
    data.append( np.genfromtxt(filename[i], delimiter=','))
    data[i] = data[i][data[i] != 0]
    data[i] = data[i][~np.isnan(data[i])]

outfile = sys.argv[(1+no_files)*2+1]

for i in range(0, no_files):
    cdf(data[i][:-2], file_desc[i], outfile)


plt.show()

