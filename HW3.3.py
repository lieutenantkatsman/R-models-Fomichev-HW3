import matplotlib.pyplot as plt
from scipy.misc import derivative
from math import *
import numpy as np

def f(x):
    # return eval(input())
    return sin(x)

plt.grid(True)

x = [i / 25 for i in range(-100, 100, 1)]
y = [f(i) for i in x]
y1 = [derivative(f, i, dx=1e-4) for i in x]

location = ['upper left']
plt.plot(x, y, label='y = sin x')
plt.plot(x, y1, label='y = d(sin x)')
plt.legend(loc = location[0])
plt.show()