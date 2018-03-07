## Lab04
https://github.com/linnil1/2017_BIME_sensor/tree/master/lab04

### Calibration of Temperature Transducers
Use linear regression to fit the data, and output slope and intercept in 99% confidence interval and $R^2$.

Code of `Thermo_calibration.py`
``` python3=34
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
```

### Data
Water temperature got from Iron-constantan thermocouple(TC) and
Platinum resistanc temperature detector(RTD) compared to reference data from alcohol thermometer.
see `log2.txt` `log3.txt`
First column is Temperature, second is data from TC, and third is RTD.

### Result
![](https://github.com/linnil1/2017_BIME_sensor/raw/master/lab04/Cali_TC.jpg)
![](https://github.com/linnil1/2017_BIME_sensor/raw/master/lab04/Cali_RTD.jpg)
