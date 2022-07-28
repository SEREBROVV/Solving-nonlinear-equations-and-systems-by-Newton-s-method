import math

def func(a):
    return 1 / math.tan(a) - a * a

def func_derivative(a):
    return -1 / (math.sin(a) * math.sin(a)) - 2 * a

def root_localization(a, b):
    # последовательный перебор
    n = 10
    while True:
        h = (b-a)/n
        for k in range(n+1):
            x_k = a+k*h
            x_k1 = a+(k+1)*h
            if x_k == 0 and func(a+(k-1)*h)*func(x_k1) < 0:
                return [a+(k-1)*h, x_k1]
            if x_k1 == 0 and func(x_k)*func(a+(k+2)*h)<0:
                return [x_k, a+(k+2)*h]
            if x_k != 0 and x_k1 != 0:
                if func(x_k)*func(x_k1) < 0:
                    return [x_k, x_k1]
        n *= 2

def main_method(e):
    a, b = root_localization(-10, 10)
    x = [a]
    k = 0
    a0 = a
    b0 = b
    while True:
        x_k = x[k]-func(x[k])/func_derivative(x[k])
        if not (a0 <= x_k <= b0):
            x.append(a0 - ((b0-a0)/(func(b0)-func(a0)))*func(a0))
        else:
            x.append(x_k)
        k += 1
        c = func(x[k])*func(b0)
        if c < 0:
            b0 = x[k]
        elif c > 0:
            a0 = x[k]
        if abs(x[k]-x[k-1]) < e:
            break

    return x[k]

x = main_method(1e-10)
print(f'Решение: {x}. Значение функции в этой точке : {func(x)}')


