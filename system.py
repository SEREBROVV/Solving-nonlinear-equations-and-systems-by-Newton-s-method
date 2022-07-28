import math

from lup import *

def f(l, x):
    return [l * math.cos(x[0] + 0.5) + x[1] - 0.8, - 2 * x[0] + l * math.sin(x[1]) - 1.6]

def f_j(l, x):
    return[[-l * math.sin(x[0] + 0.5), 1],[-2, l * math.cos(x[1])]]

x = [-0.8, 0.8]
n = 10
for i in range(1, n+1):
    arr = f_j(i/n, x)
    b = [-f(i/n, x)[0], -f(i/n, x)[1]]
    x_newton = lup(arr, b, 2)
    x[0] = x[0] + x_newton[0]
    x[1] = x[1] + x_newton[1]
print(x)

while True:
    x_newton = lup(f_j(1, x), [- f(1, x)[0], - f(1, x)[1]], 2)
    print('x_newton:', x_newton)
    x[0] = x[0] + x_newton[0]
    x[1] = x[1] + x_newton[1]
    print('x', x)
    if (x_newton[0] ** 2 + x_newton[1] ** 2) ** (1 / 2) < 1e-4:
        break

print(f'Решение системы : {x}. Значение уравнений системы в этой точке : {f(1, x)}')
