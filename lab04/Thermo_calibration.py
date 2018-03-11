import matplotlib.pyplot as plt
from pprint import pprint
from scipy.stats import linregress, t
import numpy as np
import scipy.stats


def readfile(f):
    arr = []
    pre = ""
    tmparr = []
    for line in f:
        l = line.split()
        if l[0] != pre:
            if tmparr:
                arr.append((pre, np.array(tmparr,dtype=np.float)))
            pre = l[0]
            tmparr = []
        tmparr.append([l[1], l[2]])
    if tmparr:
        arr.append((pre, np.array(tmparr,dtype=np.float)))
    return arr

def plotOne(arr):
    # data analysis
    x = []
    y = []
    ystd = []
    for temp, num in arr:
        x.append(temp)
        y.append(num.mean())
        ystd.append(num.std())
    x = np.array(x, dtype=np.float)
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    # confidence of slope and intercept
    # https://en.wikipedia.org/wiki/Simple_linear_regression
    n = len(arr)
    sb = np.sqrt(np.sum((y - slope * x - intercept) ** 2) \
                 / np.sum((x - np.average(x)) ** 2) / (n + 2))
    std_b = sb * t.ppf(0.995, len(arr))
    sa = np.sqrt(np.sum((y - slope * x - intercept) ** 2) * np.sum(x ** 2) \
                 / n / (n + 2) / np.sum((x - np.average(x)) ** 2 ))
    std_a = sa * t.ppf(0.995, len(arr))

    # plot
    text = 'slope = {:.3}±{:.3}\nintercept = {:.3}±{:.3}\nr_squre = {:.3}'.format(
            slope, std_b, intercept, std_a, r_value**2)
    plt.text(.50, .05, text,
        horizontalalignment='center',
        verticalalignment='bottom',
        transform=plt.gca().transAxes)
    plt.plot(x, slope * x + intercept, label="fit line")
    plt.errorbar(x, y, yerr=ystd, label="measured data", ecolor='red', capsize=2)
    plt.legend(loc = 0)

# main
arr = []
with open("log2.txt") as f:
    arr.extend(readfile(f))
with open("log3.txt") as f:
    arr.extend(readfile(f))

arr0 = []
for temp, num in arr:
    arr0.append((temp, num[:, 0]))
arr1 = []
for temp, num in arr:
    if any(num[:, 1] < 3):
        arr1.append((temp, num[:, 1]))


plt.figure()
plotOne(arr0)
plt.title("TC")
plt.savefig("Cali_TC.jpg")
plt.figure()
plotOne(arr1)
plt.title("RTD")
plt.savefig("Cali_RTD.jpg")

plt.show()
