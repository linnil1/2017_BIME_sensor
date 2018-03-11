import numpy as np
import matplotlib.pyplot as plt

f = 150 # frequency
period_point = 10 # how many point each sampling interval
period = 50
sf = 200 * period // f # sampling times
t = np.linspace(0, period * 1 / f, period_point * sf)
fun = 4 * np.sin(100 * np.pi * t) + 4 * np.sin(300 * np.pi * t)

bit = 12 # bits for coding
Q = 8 * 2 / ( 2 ** bit - 1) # quantization interval

ADCout = []
for i in range(sf):
    code = np.floor((fun[i * period_point]) / Q) * Q
    ADCout.extend([code] * period_point)

plt.rc('text', usetex=True)
plt.subplot(211)
plt.title(r"4\sin(100\pi t) + 4\sin(300\pi t)")
plt.plot(t, fun)
plt.subplot(212)
plt.title("ADC output with sampling rate 200Hz")
plt.plot(t, ADCout)
# plt.legend()
plt.savefig("ADC_2.png")
plt.show()
