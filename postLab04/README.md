## postLab04
https://github.com/linnil1/2017_BIME_sensor/tree/master/postLab04

### Use linear regression analysis and report the line-fitting parameter estimates ($𝑎̂_1$, $𝑎̂_0$, $𝜎̂_𝑛$, adjusted $𝑅^2$, and unadjusted $𝑅^2$)

use `scipy.stat` can perform linear regression

code snap of `postLab04.py`
``` python3=25
slope, intercept, r_value, p_value, std_err = linregress(x, y)
n = len(x)

# r_value calculate with / (n - 1)
resdiual = -y + x * slope + intercept
var = np.sum(resdiual ** 2) / (n - 2) 
r = 1 - var / (np.std(y, ddof=1) ** 2)
un_r = 1 - (1- r) * (n - 2) / (n - 1)

# linearity and hysteresis
non_linear = np.max(np.abs(resdiual)) / (y.max() - y.min())
hysteresis = np.max(np.abs(y[:n//2] - y[n//2:])) / (y.max() - y.min())
```

### Data
Data got from problem description.
First three columns are for A, the others are B.
Column title: Temperature, Vup(mV), Vdown(mV)
``` python3
data = """
24  40  40  0   30  30 ;
30  50  58  10  40  45 ;
33  60  67  20  45  49 ;
45  68  77  30  50  52 ;
47  76  89  40  55  59 ;
55  84  90  50  62  65 ;
60  92  92  60  67  67 
"""
```

### result
![](https://github.com/linnil1/2017_BIME_sensor/raw/master/postLab04/postlab04_A.png)
![](https://github.com/linnil1/2017_BIME_sensor/raw/master/postLab04/postlab04_B.png)
