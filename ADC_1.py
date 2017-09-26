import numpy as np
import matplotlib.pyplot as plt

f = 5 # frequence
A = 10 # amplitude

sf = 50 # sampling frequence
t = np.linspace(0, 1/f, 10 * sf)
fun = A * np.sin(f * 2 * np.pi * t)

bit = 12 # bits for coding
Q = A * 2 / ( 2 ** bit - 1) # quantization interval
ADCout = []
for i in range(sf):
    code = np.floor((fun[i * 10] + Q / 2) / Q) * Q
    ADCout.extend([code] * 10)


plt.rc('text', usetex=True)
plt.plot(t, fun, label=r"10\sin(10\pi t)")
plt.plot(t, ADCout, label="ADCoutput(50Hz)")
plt.legend()
plt.show()
