import sys
import numpy as np

filename = sys.argv[1]
final_list = []
#data = []

#with open(sys.argv[1]) as f:

data = np.genfromtxt(filename, delimiter=',')
data = data[data != 0]
data.sort()

five = data[int(0.05 * len(data))]
nine_five = data[int(0.95 * len(data))]


thefile = open(sys.argv[2], 'a')
thefile.write("%s, "%five)
thefile.write("%s, \n"%nine_five)
