import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy.stats as st

us = [4.891, 4.892, 4.893, 4.894, 4.895, 4.896, 4.897, 4.898 , 4.8985, 4.899]
height = [15, 751, 878, 475, 145, 734, 1670, 220, 89, 25]
assert(len(us) == len(height))
n = np.sum(height)
u = 4.8952
s = 0.001749

# cal bin range
estimate_range = [u - s * 10] # -np.inf]
for i in range(1, len(us)):
    estimate_range.append((us[i-1] + us[i])/2)
estimate_range.append(u + s * 10) # np.inf
estimate_range = np.array(estimate_range)
center = (estimate_range[:-1] + estimate_range[1:]) / 2
width = -estimate_range[:-1] + estimate_range[1:]
print(estimate_range)

def myplot(y):
    plt.xlim(us[0] * 2 - us[1], us[-1] * 2 - us[-2])
    plt.ylim(0, n)
    plt.bar(center, y, width=width, align='center', alpha=0.5)

plt.subplot(211)
plt.title("real height")
myplot(height)

plt.subplot(212)
plt.title("Estimate height")

# cal probility in bin size
estimate_normal = (np.array(estimate_range) - u) / s
estimate_height = st.t.cdf(estimate_normal[1:], n) - st.t.cdf(estimate_normal[:-1], n)
estimate_height *= n
myplot(estimate_height)

# plot gaussion
x = np.linspace(u - 3 * s, u + 3 * s, 100)
y = np.exp(- (x - u) ** 2 / 2 / s **2 ) / np.sqrt(2 * np.pi) / s
plt.plot(x, y)

# print chi-square test
print(height)
print(estimate_height)

chi_size = len(us) - 3
chi = np.abs((height - estimate_height)/estimate_height).sum() / chi_size
print(chi_size)
print(chi)

""" not correct
chi_prob = 1 - st.chi2.cdf(chi_size)
print(chi_prob)
if 0.05 < chi_prob < 0.95:
    print("Accept")
else:
    print("Reject")
"""
plt.show()
