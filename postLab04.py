import matplotlib.pyplot as plt
from pprint import pprint
from scipy.stats import linregress, t
import numpy as np
import scipy.stats

# question
data = """
24  40  40  0   30  30 ;
30  50  58  10  40  45 ;
33  60  67  20  45  49 ;
45  68  77  30  50  52 ;
47  76  89  40  55  59 ;
55  84  90  50  62  65 ;
60  92  92  60  67  67 
"""
matdata = np.array(np.matrix(data, dtype=np.float))
temp =   np.array([matdata[:, 0], matdata[:,3]])
V_up =   np.array([matdata[:, 1], matdata[:,4]])
V_down = np.array([matdata[:, 2], matdata[:,5]])

def plotOne(x, y):
    x = x.T
    y = y.T
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    n = len(x)

    # r_value calculate with / (n - 1)
    var = np.sum((-y + x * slope + intercept) ** 2) / (n - 2) 
    r = 1 - var / (np.std(y, ddof=1) ** 2)
    un_r = 1 - (1- r) * (n - 2) / (n - 1)


    # plot
    text = """
slope = {:.3}
intercept = {:.3}
variance = {:.3}
r_squre = {:.3}
unadjusted r_squre = {:.3}""".format(slope, intercept, var, r, un_r)
    plt.text(.95, .05, text,
        horizontalalignment='right',
        verticalalignment='bottom',
        transform=plt.gca().transAxes)
    plt.plot(x, slope * x + intercept, label="fit line")
    plt.plot(x, y)
    plt.legend(loc = 0)

# main
V = np.hstack([V_up, np.flip(V_down, 1)])

plt.figure()
plotOne(np.hstack([temp[0], np.flip(temp[0], 0)]), V[0])
plt.title("Label A")
plt.figure()
plotOne(np.hstack([temp[1], np.flip(temp[1], 0)]), V[1])
plt.title("Label B")

plt.show()