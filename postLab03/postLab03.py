import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy.stats as st

data = np.array("1.0006 1.0072 0.9941 0.9918 0.9986 0.9991 1.0107 0.9981 1.0011 1.0218".split(), dtype=np.float)

data1 = np.array("0.9854 1.0056 1.0041 1.0132 0.9902 0.9876 1.0094 0.9815 0.9999 1.0027".split(), dtype=np.float)

us = [data.mean(), data1.mean()]
ts = [data.std(),  data1.std() ]
n = data.size
tns = np.array(ts) / np.sqrt(n - 1)
want = 95

def gau(m, t):
    x = np.linspace(m - 3 * t, m + 3 * t, 100)
    y = np.exp(- (x - m) ** 2 / 2 / t **2 ) / np.sqrt(2 * np.pi) / t
    return (x, y)

matplotlib.rc('figure', figsize=(10, 10))

for i in range(len(us)):
    plt.title("Batch 382")
    # plot main
    tn = tns[i]
    x, y = gau(us[i], tn)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('p(x)')
    mytext = 'mean: ' +str(us[i]) + "\n" + \
             'std:  ' +str(ts[i]) + "\n" + \
             'n:    ' +str(n    ) + "\n" + \
             r' $\sigma_{\hat{x}}$ :    ' + str(tn) + "\n"
    plt.text(1, 1, mytext,
         horizontalalignment='right',
         verticalalignment='top',
         transform = plt.gca().transAxes)

    # cal interval
    Q = st.t.ppf(want/200 + 0.5, n - 1)
    Qmin = us[i] - Q * tn
    Qmax = us[i] + Q * tn
    interval = np.logical_and(Qmin <= x, Qmax >= x)

    # plot interval
    plt.fill_between(x, y, where=interval)
    plt.text(x[50], y[50] / 2, str(want) + "%", 
             horizontalalignment='center' , color='white', size=30)

    left = np.min(np.where(interval))
    right = np.max(np.where(interval))
    plt.text(x[left],  y[left],  str(np.around(Qmin, 7)), 
             horizontalalignment='right', verticalalignment='bottom', size=10)
    plt.text(x[right], y[right], str(np.around(Qmax, 7)), 
             horizontalalignment='left' , verticalalignment='bottom', size=10)

    plt.savefig("test_" + str(i + 1) + ".jpg")
    plt.show()

plt.title("Is overlap")
plt.xlabel('x')
plt.ylabel('p(x)')
texts = ["Batch 117", "Batch 384"]
colors = ["blue", "green"]
for i in range(len(us)):
    # plot main
    tn = tns[i]
    x, y = gau(us[i], tn)

    # cal interval
    Q = st.t.ppf(want/200 + 0.5, n - 1)
    Qmin = us[i] - Q * tn
    Qmax = us[i] + Q * tn
    interval = np.logical_and(Qmin <= x, Qmax >= x)

    # plot interval
    plt.plot(x[interval], y[interval], color=colors[i])
    plt.fill_between(x[interval], y[interval], color=colors[i])
    left = np.min(np.where(interval))
    right = np.max(np.where(interval))
    plt.text(x[left],  y[left],  str(np.around(Qmin, 7)), size=10)
    plt.text(x[right], y[right], str(np.around(Qmax, 7)), size=10)

    # plot text
    plt.text(x[50], y[50], texts[i],
             horizontalalignment='center' , color=colors[i], size=30)
    plt.text(x[50], 0, "mean= " + str(us[i]),
             color='black', size=10)
plt.show()

plt.xlabel('x')
plt.ylabel('p(x)')
texts = ["Batch 117", "Batch 384"]
colors = ["blue", "green"]
for i in range(len(us)):
    tn = tns[i]
    x, y = gau(us[i], tn)
    plt.title(texts[i])
    patch = mpatches.Patch(color=colors[0], label="n = 10")
    patch1 = mpatches.Patch(color=colors[1], label="n = 100")
    plt.legend(handles=[patch, patch1])
    for j, s in enumerate([n, 100]): # the range of 10 is larger than 100
        # plot main
        # cal interval
        Q = st.t.ppf(want/200 + 0.5, s - 1)
        Qmin = us[i] - Q * tn
        Qmax = us[i] + Q * tn
        interval = np.logical_and(Qmin <= x, Qmax >= x)

        # plot interval
        plt.fill_between(x, y, where=interval, color=colors[j])
        left = np.min(np.where(interval))
        right = np.max(np.where(interval))
        
        # plot text
        plt.text(x[left],  y[left],  str(np.around(Qmin, 7)), size=10)
        plt.text(x[right], y[right], str(np.around(Qmax, 7)), size=10)

    plt.savefig("test_" + str(i + 3) + ".jpg")
    plt.show()
