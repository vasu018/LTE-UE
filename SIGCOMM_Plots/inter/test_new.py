import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO
s = StringIO(u"""     SDResource     SLOViolation
RR+RR        7.85   4.25
Inter+RR     23.7   6.92
RR+Intra     9.25   12.35
Inter+Intra  25.75   17.89""")
df = pd.read_csv(s, index_col=0, delimiter=' ', skipinitialspace=True)

_ = df.plot( kind= 'bar' , secondary_y= 'amount' , rot= 0 )
plt.show()
