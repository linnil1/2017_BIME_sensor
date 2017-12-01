import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from  scipy.ndimage.filters import uniform_filter


temp = [[20.5, 56], [55.5, 21], [21, 76], [76, 22], [21.5, 68], [68, 22]]

for num in range(6):
    # read
    datas = []
    with open("lab05log" + str(num + 7) + ".txt") as f:
        for line in f:
            datas.append(float(line.split()[2]))

    # normalized
    data = uniform_filter(datas, size=10)
    data_init = np.mean(data[:100])
    data_end  = np.mean(data[-100:])
    data = (data_end - np.array(data)) / (data_end - data_init)

    # get raise data
    raise_data = data[(data>0.2) & (data<0.9)]
    log_data = np.log(raise_data)
    slope, intercept, r_value, p_value, std_err = \
        linregress(10 * np.arange(len(raise_data)), log_data)
    text = 'slope = {:.3}\nr_squre = {:.3}'.format(slope, r_value**2)

    # plot 
    plt.figure(num, figsize=(20, 10), dpi=80)
    plt.subplot2grid((2, 2), (0, 0), colspan=2)
    plt.plot(datas)
    plt.title("Orignial data")
    plt.xlabel("time (x10ms)")
    plt.ylabel("Voltage")
    plt.text(.95, .05, "K : {:.3}".format(np.abs((data_init - data_end) / 
                                                 (temp[num][0] -temp[num][1]))),
             horizontalalignment='right',
             verticalalignment='bottom',
             transform=plt.gca().transAxes)

    plt.subplot(223)
    plt.plot(log_data)
    plt.plot(np.arange(len(raise_data)) * slope * 10 + intercept)
    plt.title("log(y) vs t")
    plt.xlabel("time (x10ms)")
    plt.ylabel(r"$\log((y(t)-y_0)/(y_e-y_0))$")
    plt.text(.95, .95, text,
             horizontalalignment='right',
             verticalalignment='top',
             transform=plt.gca().transAxes)

    plt.subplot(224)
    plt.plot(data)
    plt.title("Normalized data")
    plt.plot(np.repeat(0, len(data)))
    plt.plot(np.repeat(1, len(data)))
    plt.xlabel("time (x10ms)")
    plt.ylabel(r"Abs $y_e - y(t)$")

    # save it or plot it
    plt.suptitle("Data {}: Temperture: {} to {}".format(num, *temp[num]))
    plt.savefig("log5_data_" + str(num) + ".jpg")
    plt.clf()
    # plt.show()
