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
    step = 1
    # parameters
    n = 2
    N = 10
    F = 0.5
    P = 0.7
    X = [0 for i in range(2 * N)]
    X_M = [0, 0]
    X_T = [0, 0]
    T = []

    while 1:
        if step == 1:
            # step 1
            for i in range(0, 2 * N, 2):
                X[i] = random.uniform(left, right)
                X[i + 1] = random.uniform(left, right)
            step = 2

        if step == 2:
            # step 2
            i = 0
            step = 3

        if step == 3:
            # step 3
            X_A = X[0:3]
            X_B = X_A[:]
            X_C = X_A[:]
            while X_A == X_B or X_A == X_C or X_B == X_C and X_A == X[i * 3:i * 3 + 3] and X_B == X[i * 3:i * 3 + 3] and X_C == X[i * 3:i * 3 + 3]:
                temp_a = random.randint(0, N - 1)
                temp_b = random.randint(0, N - 1)
                temp_c = random.randint(0, N - 1)
                X_A = X[temp_a * 2:temp_a * 2 + 2]
                X_B = X[temp_b * 2:temp_b * 2 + 2]
                X_C = X[temp_c * 2:temp_c * 2 + 2]

            # step 4
            X_M[0] = X_C[0] + F * (X_A[0] - X_B[0])
            X_M[1] = X_C[1] + F * (X_A[1] - X_B[1])

            # step 5
            k = 1

        # step 6
        p = random.uniform(0, 1)

        # step 7
        if p < P:
            X_T[k - 1] = X_M[k - 1]
        else:
            X_T[k - 1] = X[i * 2 + k - 1]

        # step 8
        k += 1

        # step 9
        if k <= n:
            step = 6
            continue

        # step 10
        f_t = -0.0001 * (abs(np.sin(X_T[0]) * np.sin(X_T[1]) * np.exp(abs(100 - (X_T[0] ** 2 + X_T[1] ** 2) ** 0.5 / np.pi))) + 1) ** 0.1
        f_i = -0.0001 * (abs(np.sin(X[i * 2]) * np.sin(X[i * 2 + 1]) * np.exp(abs(100 - (X[i * 2] ** 2 + X[i * 2 + 1] ** 2) ** 0.5 / np.pi))) + 1) ** 0.1

        if f_t < f_i:
            T.append(X_T[0])
            T.append(X_T[1])
            step = 12
        else:
            # step 11
            T.append(X[i * 2])
            T.append(X[i * 2 + 1])

        # step 12
        i += 1

        # step 13
        if i <= N - 1:
            step = 3
            continue

        # step 14
        X = T
        T = []

        # step 15
        t = 0
        for ii in range(0, N):
            for jj in range(0, N):
                if ii != jj:
                    distance = np.linalg.norm(np.array(X[jj * 2:jj * 2 + 2]) - np.array(X[ii * 2:ii * 2 + 2]))
                    if distance < e:
                        t += 1
        if t == N ** 2 - N:
            X_M = X[0:2]
            break

        # step 16
        step = 2

    print(f"\n\t x_min = {X_M[0]} y_min = {X_M[1]} f_min = {-0.0001 * (abs(np.sin(X_M[0]) * np.sin(X_M[1]) * np.exp(abs(100 - (X_M[0] ** 2 + X_M[1] ** 2) ** 0.5 / np.pi))) + 1) ** 0.1}")
    plt.scatter(X_M[0], X_M[1], c="b")
    t2 = time.time() - t1
    print(f"\n\tExecution time = {t2} seconds")
    plt.show()
