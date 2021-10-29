"""
алгоритм пчелиной колонии (глобальная оптимизация)
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import random
import copy
from scipy.optimize import fmin

if __name__ == "__main__":
    # построение графика функции
    x, y = np.mgrid[-10:10:0.1, -10:10:0.1]
    f = -0.0001 * (abs(np.sin(x) * np.sin(y) * np.exp(abs(100 - (x ** 2 + y ** 2) ** 0.5 / np.pi))) + 1) ** 0.1
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, f, cmap="viridis")
    plt.title("График поверхности")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    fig1 = plt.contour(x, y, f, 25)
    plt.clabel(fig1, inline='True')
    plt.title("Поиск минимума методом пчелиной колонии")
    t1 = time.time()
    # метод пчелиной колонии
    e = 0.0001
    t_max = 0
    left = -10
    right = 10
    step = 0
    flag = 0
    optim_count = 0
    iterations = 0
    # parameters
    s = 10
    X = np.zeros((3, s))
    B = 3
    G = 3
    b = 2
    g = 2
    R = 1
    x_m = 0
    y_m = 0
    f_m = 0
    while flag < 1:
        iterations += 1
        if step != 3 and step != 4:
            # step 1
            for i in range(0, s):
                X[0][i] = random.uniform(left, right)
                X[1][i] = random.uniform(left, right)
                X[2][i] = -0.0001 * (abs(np.sin(X[0][i]) * np.sin(X[1][i]) * np.exp(abs(100 - (X[0][i] ** 2 + X[1][i] ** 2) ** 0.5 / np.pi))) + 1) ** 0.1
        # print("X:\n", X)
        # print("---------------")

            # step 2
            f_m = min(X[2][:])
            arg = np.argmin(X[2][:])
            x_m = X[0][arg]
            y_m = X[1][arg]

            step = 3

            # print(f_m)
            # print("---------------")

        if step == 3:
            # step 3
            t = 0
            step = 4

        if step == 4:
            # step 4
            for i in range(0, s - 1):
                for j in range(0, s - 1):
                    if X[2][j] > X[2][j + 1]:
                        X[0][j], X[0][j + 1] = X[0][j + 1], X[0][j]
                        X[1][j], X[1][j + 1] = X[1][j + 1], X[1][j]
                        X[2][j], X[2][j + 1] = X[2][j + 1], X[2][j]
        X_B = X[:, 0:B]
        # print("X_B:\n", X_B)
        # print("---------------")

        # step 5
        X_b = np.zeros((3, B * b))
        k = 0
        for i in range(0, B):
            for j in range(0, b):
                X_b[0][k] = random.uniform(X_B[0][i] + R, X_B[0][i] - R)
                X_b[1][k] = random.uniform(X_B[1][i] + R, X_B[1][i] - R)
                X_b[2][k] = -0.0001 * (abs(np.sin(X_b[0][k]) * np.sin(X_b[1][k]) * np.exp(abs(100 - (X_b[0][k] ** 2 + X_b[1][k] ** 2) ** 0.5 / np.pi))) + 1) ** 0.1
                k += 1

        # print("X_b:\n", X_b)
        # print("---------------")

        # step 6
        X_G = X[:, B:B + G]
        # print("X_G:\n", X_G)
        # print("---------------")

        # step 7
        X_g = np.zeros((3, G * g))
        k = 0
        for i in range(0, G):
            for j in range(0, g):
                X_g[0][k] = random.uniform(X_G[0][i] + R, X_G[0][i] - R)
                X_g[1][k] = random.uniform(X_G[1][i] + R, X_G[1][i] - R)
                X_g[2][k] = -0.0001 * (abs(np.sin(X_g[0][k]) * np.sin(X_g[1][k]) * np.exp(abs(100 - (X_g[0][k] ** 2 + X_g[1][k] ** 2) ** 0.5 / np.pi))) + 1) ** 0.1
                k += 1
        # print("X_g:\n", X_g)
        # print("---------------")

        # step 8
        X_s = np.zeros((3, s - B - G))
        # print("X_s:\n", X_s)
        for i in range(0, s - B - G):
            X_s[0][i] = random.uniform(left, right)
            X_s[1][i] = random.uniform(left, right)
            X_s[2][i] = -0.0001 * (abs(np.sin(X_s[0][i]) * np.sin(X_s[1][i]) * np.exp(abs(100 - (X_s[0][i] ** 2 + X_s[1][i] ** 2) ** 0.5 / np.pi))) + 1) ** 0.1
        # print("X_s:\n", X_s)
        # print("---------------")

        # step 9
        X = []
        X = [X_B[:, :], X_G[:, :], X_b[:, :], X_g[:, :], X_s[:, :]]
        # print("X:\n", X)

        # step 10
        # error ########################################################################################################
        f_x = X[2][0]
        for i in range(1, len(X)):
            if X[2][i] < f_x:
                x_x = X[0][i]
                y_x = X[1][i]
                f_x = X[2][i]
        # plot

        # step 11
        if f_x < f_m:
            x_m = x_x
            y_m = y_x
            f_m = f_x
            step = 3

        if step != 3:
            # step 12
            t = t + 1

            # step 13
            if t < t_max:
                step = 4

            # step 14
            if step != 4:
                if R < e:
                    flag = 1
                    print(X[0][0], X[1][0])

            # step 15
            R = R / 2
            step = 4


    t2 = time.time() - t1
    print(f"\tExecution time = {t2} seconds")
    plt.show()