"""
метод Фибоначчи (одномерная безусловная оптимизация)
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import time

def Fibonacci(n):
    temp = 1
    if n > 2:
        temp = Fibonacci(n - 1) + Fibonacci(n - 2)
    return temp

if __name__ == "__main__":
    # построение графика функции
    x = np.arange(0, np.pi / 2, 0.01 * np.pi)
    y = np.zeros(len(x))
    i = 0
    for i in range(len(x) - 1):
        y[i] = 15 * (2.25 - math.sin(x[i])) / (math.cos(x[i]))
    plt.plot(x[0:len(x) - 1], y[0:len(x) - 1], color='green')

    t1 = time.time()
    # метод Фибоначчи
    A = 0
    B = np.pi / 2
    e = 0.01
    y_i = np.zeros((4, 1))
    t = 2
    iter = 0
    # step 1
    y_i[0] = 15 * (2.25 - np.sin(A)) / (np.cos(A))
    y_i[1] = 15 * (2.25 - np.sin(B)) / (np.cos(B))
    n = 1
    while 1:
        if t == 2:
            # step 2
            while Fibonacci(n) < (B - A) / e:
                n += 1
            # step 3
            C = B - (B - A) * Fibonacci(n - 1) / Fibonacci(n)
            D = B - (C - A)
            # step 4
            y_i[2] = 15 * (2.25 - np.sin(C)) / (np.cos(C))
            y_i[3] = 15 * (2.25 - np.sin(D)) / (np.cos(D))
        # step 5
        f_min = np.min(y_i)
        for i in range(len(y_i) - 1):
            if y_i[i] == f_min:
                x_min = i
        n -= 1
        # step 6
        if n == 2:
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
            print(f"\tf_min = {f_min}")
            break
        else:
            # step 7
            if x_min == 0:
                A = A
                B = C
                y_i[1] = y_i[2]
                t = 2
            if x_min == 1:
                A = D
                B = B
                y_i[0] = y_i[3]
                t = 2
            if x_min == 2:
                A = A
                B = D
                D = C
                C = A + (B - D)
                y_i[1] = y_i[3]
                y_i[3] = y_i[2]
                y_i[2] = 15 * (2.25 - np.sin(C)) / (np.cos(C))
                t = 5
            if x_min == 3:
                A = C
                B = B
                C = D
                D = B - (C - A)
                y_i[0] = y_i[2]
                y_i[2] = y_i[3]
                y_i[3] = 15 * (2.25 - np.sin(D)) / (np.cos(D))
                t = 5
        iter += 1
        print(f"iter = {iter}\tA = {A}\tf(A) = {y_i[0]}\tB = {B}\tf(B) = {y_i[1]}\tC = {C}\tf(C) = {y_i[2]}\tD = {D}\tf(D) = {y_i[3]}\tn = {n}")
        plt.plot([A, A, B, B], [0, 200 - iter * 10, 200 - iter * 10, 0])

    t2 = time.time() - t1
    print(f"\tExecution time = {t2} seconds")
    plt.scatter(x_min, f_min, c='black')
    plt.text(x_min, f_min + 5, "Точка минимума")
    plt.title("График целевой функции для метода Фибоначчи")
    plt.show()
