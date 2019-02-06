import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib

f = plt.figure()
def time(data_set, Label, outfile):
    global f
    data_size=len(data)

    print len(data_set)
    y_pos = np.arange(min(data_set), max(data_set)+1, int(max(data_set)/20))
    #plt.bar(y_pos, data_set, align='center', alpha=0.5)
    plt.plot(data_set, label=Label)
#only 5 ticks
#    plt.xticks(np.arange(0, len(data_set), len(data_set)/5))
    plt.ylabel("Latency(ms)")
    plt.xlabel("Requests over time")
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

matplotlib.interactive(True)
no_files = int(sys.argv[2])

for i in range(0, no_files):
    file_desc.append(sys.argv[2 + (i*2 + 1)])
    filename.append(sys.argv[2 + (i*2 + 2)])
    data.append( np.genfromtxt(filename[i], delimiter=','))
    data[i] = data[i][data[i] != 0]
    data[i] = data[i][~np.isnan(data[i])]

outfile = sys.argv[(1+no_files)*2+1]

for i in range(0, no_files):
    time(data[i][:-2], file_desc[i], outfile)


plt.show()

