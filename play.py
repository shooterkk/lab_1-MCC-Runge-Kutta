import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import rk4
from math import atan, cos


h = 0.001
t_max = 100
t = np.arange(0, t_max+h, h)

b = 0.01
w0 = 0.5

x0 = 5
y0 = 0

f0 =0
w = 0.2



def f_out(t, x, y):
   return f0*np.cos(w*t) - 2*b*y - w0**2*x

def f_in(x, y):
    return -2*b*y - w0*w0*x

def f(t, x):
    return t


x = np.zeros(len(t), dtype = float)
y = np.zeros(len(t), dtype = float)
x[0] = x0
y[0] = y0

phi = atan(-y0/(w0*x0))
A0 = x0/(cos(atan(phi)))
x_real = A0*np.exp(-b*t)*np.cos(t*np.sqrt(w0*w0-b*b) + phi)

for i in range(1, len(t)):
    y[i] = rk4.rk4(x[i-1], y[i-1], f_in, h)
    x[i] = rk4.rk4(y[i-1], x[i-1], f, h)



a = plt.subplot(311)
plt.plot(t, x_real)
plt.xlabel(r'$t$')
plt.ylabel(r'$x_real$')
plt.grid(True)

plt.subplot(312)
plt.plot(t, x)
plt.xlabel(r'$t$')
plt.ylabel(r'$dev(x)$')
plt.grid(True)


plt.subplot(313)
plt.plot(t, y)
plt.xlabel(r'$x$')
plt.ylabel(r'$x$')
plt.grid(True)
plt.legend(lob ='upper right')

plt.show()



