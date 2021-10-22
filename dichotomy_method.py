"""
метод дихотомии (одномерная безусловная оптимизация)
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
    # метод дихотомии
    A = 0
    B = np.pi / 2
    e = 0.01
    y_i = np.zeros((5, 1))
    t = 2
    n = 0
    # step 1
    y_i[0] = 15 * (2.25 - np.sin(A)) / (np.cos(A))
    y_i[1] = 15 * (2.25 - np.sin(B)) / (np.cos(B))
    while 1:
        # step 2
        if t == 2:
            C = A + (B - A) / 2
            # step 3
            y_i[2] = 15 * (2.25 - np.sin(C)) / (np.cos(C))
        # step 4
        D = A + (C - A) / 2
        E = C + (B - C) / 2
        # step 5
        y_i[3] = 15 * (2.25 - np.sin(D)) / (np.cos(D))
        y_i[4] = 15 * (2.25 - np.sin(E)) / (np.cos(E))
        # step 6
        f_min = np.min(y_i)
        for i in range(len(y_i) - 1):
            if y_i[i] == f_min:
                x_min = i
        # step 7
        if B - A < e:
            if x_min == 0:
                print(f"\n\tx_min = {A}")
                x_min = A
            if x_min == 1:
                print(f"\n\tx_min = {B}")
                x_min = B
            if x_min == 2:
                print(f"\n\tx_min = {C}")
                x_min = C
            if x_min == 3:
                print(f"\n\tx_min = {D}")
                x_min = D
            if x_min == 4:
                print(f"\n\tx_min = {E}")
                x_min = E
            print(f"\tf_min = {f_min}")
            break
        else:
            # step 8
            if x_min == 0:
                A = A
                B = D
                y_i[1] = y_i[3]
                t = 2
            if x_min == 1:
                A = E
                B = B
                y_i[0] = y_i[4]
                t = 2
            if x_min == 2:
                A = D
                B = E
                y_i[0] = y_i[3]
                y_i[1] = y_i[4]
                t = 4
            if x_min == 3:
                B = C
                C = D
                y_i[1] = y_i[2]
                y_i[2] = y_i[3]
                t = 4
            if x_min == 4:
                A = C
                C = E
                y_i[0] = y_i[2]
                y_i[2] = y_i[4]
                t = 4
        n = n + 1
        print(f"n = {n}\tA = {A}\tf(A) = {y_i[0]}\tB = {B}\tf(B) = {y_i[1]}\tC = {C}\tf(C) = {y_i[2]}\tD = {D}\tf(D) = {y_i[3]}\tE = {E}\tf(E) = {y_i[4]}")
        plt.plot([A, A, B, B], [0, 200 - n * 10, 200 - n * 10, 0])

    t2 = time.time() - t1
    print(f"\tExecution time = {t2} seconds")
    plt.scatter(x_min, f_min, c='black')
    plt.text(x_min, f_min + 5, "Точка минимума")
    plt.title("График целевой функции для метода дихотомии")
    plt.show()