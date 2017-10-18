import matplotlib.pyplot as plt
import numpy as np
sample_num = 100
lim = [0, 0.05]

x = np.linspace(-1, 1, sample_num)
plt.subplot(211)
num = np.arcsin(x[1:]) - np.arcsin(x[:-1])
plt.plot(x[:-1], num/2)
plt.title("formula")
plt.ylim(lim)

plt.subplot(212)
x = np.linspace(0, 2*np.pi, sample_num)
y = np.sin(x)
weights = np.ones_like(y)/float(len(y))
plt.hist(y, weights=weights, bins=sample_num)
plt.ylim(lim)
plt.title("histogram")
plt.savefig("sin_adc_bin.jpg")
plt.show()
