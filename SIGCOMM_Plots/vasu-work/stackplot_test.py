import pandas as pd

df = pd.DataFrame(dict(
    A=[1, 2, 3, 4],
    B=[2, 3, 4, 5],
    C=[3, 4, 5, 6],
    D=[4, 5, 6, 7]))

import matplotlib.pyplot as plt
#matplotlib inline
fig = plt.figure(figsize=(20, 10))

ab_bar_list = [plt.bar([0, 1, 2, 3], df.B, align='edge', width= 0.2),
               plt.bar([0, 1, 2, 3], df.A, align='edge', width= 0.2)]

cd_bar_list = [plt.bar([0, 1, 2, 3], df.D, align='edge',width= -0.2),
               plt.bar([0, 1, 2, 3], df.C, align='edge',width= -0.2)]

plt.show()
