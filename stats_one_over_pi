import math, os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.optimize import curve_fit
from collections import Counter
f = open('oneoverpi.txt','r')
num = '3'
freq = []
longstr = ''
#data preprocessing
lines = f.readlines()
for line in lines[1:]:
    longstr += line

start_idx = -1
for idx, digit in enumerate(longstr):
    if digit == num and start_idx != -1 :
        freq.append(idx - start_idx - 1)
        start_idx = idx
    elif digit == num and start_idx == -1:
        start_idx = idx
freq_arr = sorted(np.array(freq))
freq_cnt = dict(Counter(freq_arr))
x_sample = np.array(list(freq_cnt))
y_sample = np.array(list(freq_cnt.values()))

# plot
sns.set_style('darkgrid')
sns.distplot(freq_arr,kde=False)

def func(x, a, b):
    return a * np.exp(-b * x)

#xdata = np.linspace(0,112,len(freq_arr))
y_data = func(x_sample,1.0,1.3)

plt.figure('拟合图')
#plt.plot(x_sample, y_data, 'b-', label='data')
plt.plot(x_sample, y_sample, 'b-', label='data')

popt, pcov = curve_fit(func, x_sample, y_sample)
plt.plot(x_sample, func(x_sample, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

