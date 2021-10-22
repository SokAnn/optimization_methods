"""
метод золотого сечения (одномерная безусловная оптимизация)
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import time

if __name__ == "__main__":
    # построение графика функции
    x = np.arange(0, np.pi / 2, 0.01 * np.pi)
    y = np.zeros(len(x))
    i = 0
    for i in range(len(x) - 1):
        y[i] = 15 * (2.25 - math.sin(x[i])) / (math.cos(x[i]))
    plt.plot(x[0:len(x) - 1], y[0:len(x) - 1], color='green')

    t1 = time.time()
    # метод золотого сечения
    a = 0
    b = np.pi / 2
    e = 0.01
    F = (1 + math.sqrt(5)) / 2
    tt = 2
    ttt = 4
    y_i = np.zeros(4)
    t = 0
    x_min = 0
    i = 0
    n = 0
    N = 0
    x = np.zeros(50)

    # step 1
    y_i[0] = 15 * (2.25 - np.sin(a)) / (np.cos(a))
    y_i[3] = 15 * (2.25 - np.sin(b)) / (np.cos(b))
    N = N + 2
    print("\n")
    j = 0
    while t < 1:
        if tt == 2:
            # step 2
            c = b - (b - a) / F
            d = b - (c - a)

            # step 3
            y_i[1] = 15 * (2.25 - np.sin(c)) / (np.cos(c))
            y_i[2] = 15 * (2.25 - np.sin(d)) / (np.cos(d))
            N = N + 2

        # step 4
        y_min = np.min(y_i)
        i = 0
        for i in range(len(y_i) - 1):
            if y_i[i] == y_min:
                x_min = i

        if abs(b - a) < e:
            # step 5
            if x_min == 0:
                print(f"\n\tx_min = {a}")
                x_min = a
            if x_min == 3:
                print(f"\n\tx_min = {b}")
                x_min = b
            if x_min == 1:
                print(f"\n\tx_min = {c}")
                x_min = c
            if x_min == 2:
                print(f"\n\tx_min = {d}")
                x_min = d
            print(f"\ty_min = {y_min}")
            t = 1
            break
        else:
            # step 6
            if x_min == 0:
                a = a
                b = c
                y_i[3] = y_i[2]
                tt = 2
                ttt = 0
            if x_min == 3:
                a = d
                b = b
                y_i[0] = y_i[2]
                tt = 2
                ttt = 0
            if x_min == 1:
                a = a
                b = d
                d = c
                c = a + (b - d)
                y_i[3] = y_i[2]
                y_i[2] = y_i[1]
                y_i[1] = 15 * (2.25 - np.sin(c)) / (np.cos(c))
                N = N + 1
                ttt = 4
                tt = 0
            if x_min == 2:
                a = c
                b = b
                c = d
                d = b - (c - a)
                y_i[0] = y_i[1]
                y_i[1] = y_i[2]
                y_i[2] = 15 * (2.25 - np.sin(d)) / (np.cos(d))
                N = N + 1
                ttt = 4
                tt = 0
        n = n + 1
        print(f"n = {n}\ta = {a}\tf(a) = {y_i[0]}\tc = {c}\tf(c) = {y_i[1]}\td = {d}\tf(d) = {y_i[2]}\tb = {b}\tf(b) = "
              f"{y_i[3]}\tN = {N}")
        N = 0
        plt.plot([a, a, b, b], [0, 200 - n * 10, 200 - n * 10, 0])

    t2 = time.time() - t1
    print(f"\tExecution time = {t2} seconds")
    plt.scatter(x_min, y_min, c='black')
    plt.text(x_min, y_min + 5, "Точка минимума")
    plt.title("График целевой функции с интервалами поиска экстремума для метода золотого сечения")
    plt.show()
