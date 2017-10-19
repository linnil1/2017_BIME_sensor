import matplotlib.pyplot as plt
import numpy as np
sample_num = 100
lim = [0, 0.05]

x = np.linspace(-0.999999, 0.999999, sample_num)
plt.subplot(311)
num = np.arcsin(x[1:]) - np.arcsin(x[:-1])
plt.plot(x[:-1], num/2)
plt.title("derived formula")
plt.ylim(lim)

plt.subplot(312)
plt.plot(x, 1/np.sqrt(1-x**2)/sample_num)
plt.title("differential formula")
plt.ylim(lim)

plt.subplot(313)
x = np.linspace(0, 2*np.pi, sample_num)
y = np.sin(x)
weights = np.ones_like(y)/float(len(y))
plt.hist(y, weights=weights, bins=sample_num)
plt.ylim(lim)
plt.title("histogram")
plt.savefig("sin_adc_bin.jpg")
plt.show()