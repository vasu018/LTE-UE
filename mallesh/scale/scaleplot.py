import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab

data1 = []
data2 = []

count = 0
with open("./scale_data.txt", "r") as ins:
    for line in ins:
        count = count +1

print count
with open("./scale_data.txt", "r") as ins:
    for line in ins:
         
        midcount = count /2
        if count == midcount:
            
        line = line.strip()
        words = line.split(",")
        x = words[0]
        y = words[1]
        data1.append(float(x))
        data2.append(float(y))
        count = count -1

print data1, data2
plt.step(range(121), data1, color='r')
plt.scatter(range(121), data2)
plt.ylim([0, 12000])
plt.show()
