import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':36})
import scipy.stats as stats
import math
import matplotlib.mlab as mlab

mu, sigma = 500, 0.05 # mean and standard deviation
s = np.random.normal(mu, sigma, 100)

count, bins, ignored = plt.hist(s, 1000, normed=True)

f = open('dummy.txt', 'w')

for i in count:
    f.write('%s\n'%(i))

f.close()
