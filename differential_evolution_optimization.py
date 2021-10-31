"""
алгоритм дифференциальной эволюции (глобальная оптимизация)
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import random

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
    plt.title("Поиск минимума методом дифференциальной эволюции")
    t1 = time.time()
    # метод дифференциальной эволюции
    iterations = 0
    e = 0.0001
    t_max = 10
    left = -10
    right = 10
    step = 0
    # parameters
    N = 5
    F = 0.5
    P = 0.3
    X = [[0] * N for i in range(3)]
    # step 1
    for i in range(0, N):
        X[0][i] = random.uniform(left, right)
        X[1][i] = random.uniform(left, right)
        X[2][i] = -0.0001 * (abs(np.sin(X[0][i]) * np.sin(X[1][i]) * np.exp(abs(100 - (X[0][i] ** 2 + X[1][i] ** 2) ** 0.5 / np.pi))) + 1) ** 0.1
    print(X)

    # step 2
    i = 0

    # step 3 # error !!! ###############################################################################################
    X_A = X[:][i]
    X_B = X[:][i]
    X_C = X[:][i]
    print(len(X), len(X[0]))
    print(X[0][0], X[1][0], X[2][0])
    while X_A == X[:][i] and X_B == X[:][i] and X_C == X[:][i]:
        temp_a = random.randint(0, len(X[0]))
        temp_b = random.randint(0, len(X[0]))
        temp_c = random.randint(0, len(X[0]))
        X_A = X[:][temp_a]
        X_B = X[:][temp_b]
        X_C = X[:][temp_c]
    print(X_A, X_B, X_C)

    # step 4

    # step 5
    k = 1

    # step 6

    # step 7

    # step 8
    k += 1

    # step 9

    # step 10

    # step 11

    # step 12
    i += 1

    # step 13

    # step 14

    # step 15

    # step 16


    t2 = time.time() - t1
    print(f"\n\tExecution time = {t2} seconds")
    plt.show()
