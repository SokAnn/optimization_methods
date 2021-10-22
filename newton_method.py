"""
метод Ньютона (одномерная безусловная оптимизация)
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
    # метод Ньютона
    A = 0
    B = np.pi / 2
    e = 0.01
    iter = 0
    while 1:
        x_0 = np.random.uniform(A, B)
        if 15 * (2.25 * pow(np.cos(x_0), 3) + 4.5 * pow(np.sin(x_0), 2) * np.cos(x_0) - 2 * np.sin(x_0) * np.cos(x_0)) / (pow(np.cos(x_0), 4)) > 0:
            break
    while 1:
        # step 2
        x_e = x_0 - (15 * (2.25 * np.sin(x_0) - 1) / pow(np.cos(x_0), 2)) / (15 * (2.25 * pow(np.cos(x_0), 3) + 4.5 * pow(np.sin(x_0), 2) * np.cos(x_0) - 2 * np.sin(x_0) * np.cos(x_0)) / (pow(np.cos(x_0), 4)))
        # step 3
        if x_0 - x_e < e:
            x_min = x_e
            print(f"\n\tx_min = {x_min}")
            f_min = 15 * (2.25 - np.sin(x_min)) / (np.cos(x_min))
            print(f"\tf_min = {f_min}")
            break
        else:
            # step 4
            plt.plot([x_0, x_0, x_e, x_e], [0, 200 - iter * 10, 200 - iter * 10, 0])
            print(f"iter = {iter}\tx0 = {x_0}\txe = {x_e}")
            x_0 = x_e
        iter += 1

    t2 = time.time() - t1
    print(f"\tExecution time = {t2} seconds")
    plt.scatter(x_min, f_min, c='black')
    plt.text(x_min, f_min + 5, "Точка минимума")
    plt.title("График целевой функции для метода Ньютона")
    plt.show()
