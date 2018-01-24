import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab

data = np.loadtxt('data.txt', delimiter='\t', usecols=2)


c = len(data)
k = data[0]
d = []
for i in data:
    if c > 50:
        if i < k:
            i = k
    else:
        if i >= k:
            i = k
    d.append(i)
    k = i
    c -= 1

plt.step(range(100), d, color='r')
#plt.scatter(range(100), data)

plt.xlabel("Time (Seconds)")
plt.ylabel("Number of Control Procedures (K)")

plt.ylim([0, 500])
plt.show()
