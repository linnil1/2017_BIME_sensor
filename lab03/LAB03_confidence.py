import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy.stats as st

us = [4.8949, 4.8957, 4.8939, 4.8932, 4.8954]
ts = [0.0004995, 0.0004992, 0.001768, 0.001757, 0.0006654]
n = 5000
tns = np.array(ts) / np.sqrt(n - 1)
print(us)
print(ts)
print(tns)

def gau(m, t):
    x = np.linspace(m - 3 * t, m + 3 * t, 100)
    y = np.exp(- (x - m) ** 2 / 2 / t **2 ) / np.sqrt(2 * np.pi) / t
    return (x, y)

matplotlib.rc('figure', figsize=(10, 10))

for i in range(len(us)):
    plt.suptitle("measurement " + str(i + 1))
    for j,want in enumerate([99, 68]):
        # plot main
        plt.subplot(211 + j)
        tn = tns[i]
        x, y = gau(us[i], tn)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('p(x)')

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

    plt.savefig("measurement_" + str(i + 1) + ".jpg")
    plt.clf()
    # plt.show()
