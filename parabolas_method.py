"""
метод парабол (одномерная безусловная оптимизация)
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
    # метод парабол
    f_i = np.zeros((3, 1))
    x_i = np.zeros(3)
    i = 0
    j = 0
    f_min = 0
    x_min = 0
    a = np.zeros(3)
    m = np.zeros((3, 3))
    x_e = 0
    f_e = 0
    flag = 0
    x = 0
    e = 0.01
    n = 0
    N = 0

    # step 1
    while (x_i[0] >= x_i[1]) or (x_i[1] >= x_i[2]) or (f_i[0] <= f_i[1]) or (f_i[1] >= f_i[2]):
        x_i[0] = np.random.uniform(0, np.pi / 6)
        x_i[1] = np.random.uniform(np.pi / 6, np.pi / 3)
        x_i[2] = np.random.uniform(np.pi / 3, np.pi / 2)
        for i in range(len(f_i)):
            f_i[i] = 15 * (2.25 - np.sin(x_i[i])) / (np.cos(x_i[i]))
        N = N + 3

    print(x_i)
    print(f_i)

    while flag < 1:
        plt.plot([x_i[0], x_i[1], x_i[2]], [f_i[0], f_i[1], f_i[2]])
        # step 2
        i = 0
        for i in range(len(a)):
            for j in range(len(a)):
                m[i][j] = x_i[i] ** (len(a) - 1 - j)
        m = np.linalg.inv(m)
        a = m.dot(f_i)

        # step 3
        x_e = -a[1] / (2 * a[0])
        f_e = 15 * (2.25 - np.sin(x_e)) / (np.cos(x_e))
        N = N + 1

        # step 4
        f_min = np.min(f_i)
        if f_min > f_e:
            f_min = f_e

        i = 0
        for i in range(len(f_i)):
            if f_min == f_i[i]:
                x = x_i[i]
            else:
                x = x_e

        # step 5
        if abs(x_i[1] - x_e) < e:
            x_min = x_e
            flag = 1
        else:
            # step 6
            if (x == x_i[1]) and (x_e < x_i[1]):
                x_i[0] = x_e
                f_i[0] = f_e
            if (x == x_i[1]) and (x_e > x_i[1]):
                x_i[2] = x_e
                f_i[2] = f_e
            if (x == x_e) and (x_e < x_i[1]):
                x_i[2] = x_i[1]
                x_i[1] = x_e
                f_i[2] = f_i[1]
                f_i[1] = f_e
            if (x == x_e) and (x_e > x_i[1]):
                x_i[0] = x_i[1]
                x_i[1] = x_e
                f_i[0] = f_i[1]
                f_i[1] = f_e

        n = n + 1
        print(f"n = {n}\tx1 = {x_i[0]}\tf(x1) = {f_i[0]}\tx2 = {x_i[1]}\tf(x2) = {f_i[1]}\tx3 = {x_i[2]}\tf(x3) = "
              f"{f_i[2]}\txe = {x_e}\tf(xe) = {f_e}\tN = {N}")
        N = 0

    print(f"\tx_min = {x_min}")
    print(f"\tf_min = {f_min}")
    t2 = time.time() - t1
    print(f"\tExecution time = {t2} seconds")
    plt.scatter(x_min, f_min, c='black')
    plt.text(x_min, f_min + 5, "Точка минимума")
    plt.title("График целевой функции для метода парабол")
    plt.show()
