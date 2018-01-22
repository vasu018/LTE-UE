import numpy as np
from scipy.stats import poisson
from matplotlib import pyplot as plt

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=True)

#------------------------------------------------------------
# Define the distribution parameters to be plotted
mu_values = [50, 50]
linestyles = ['-', ':']

#fig, ax = plt.subplots(figsize=(5, 3.75))

c = 1
for mu, ls in zip(mu_values, linestyles):
    # create a poisson distribution
    # we could generate a random sample from this distribution using, e.g.
    #   rand = dist.rvs(1000)
    dist = poisson(mu)
    x = np.arange(1, 100)

    if c != 0:
        plt.plot(x, dist.pmf(x), linestyle=ls, color='black',
             label=r'$\mu=%i$' % mu, drawstyle='steps')
        c  = 0
    else:
        plt.plot(x, dist.pmf(x), linestyle=ls, color='blue',
                label=r'$\mu=%i$' % mu)#, drawstyle='steps')

#plt.xlim(-0.5, 30)
#plt.ylim(0, 0.4)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu)$')
plt.title('Poisson Distribution')

plt.legend()
plt.show()
