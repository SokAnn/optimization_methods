'''
метод Розенброка (многомерная безусловная оптимизация)
'''

import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.optimize import fmin

if __name__ == "__main__":
    # построение графика функции
    x1, x2 = np.mgrid[0:5:0.01, 0:5:0.01]
    y = np.sqrt(pow(x1, 2) + 4) + np.sqrt(pow((x2 - x1), 2) + 16) + np.sqrt(pow((x2 - 5), 2) + 9)
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x1, x2, y, cmap="viridis")
    plt.title("График поверхности")
    plt.xlabel("x1")
    plt.ylabel("x2")

    t1 = time.time()
    # метод Розенброка
    A1 = A2 = 0
    B1 = B2 = 5
    e = 0.001
    n = 2
    iterations = 0
    optimizations = 0
    e_i = [0, 0]
    t = 2
    flag = 0
    # init starting point & new point
    x_i_0 = [0, 2]
    x_i = x_i_0[:]
    x_ii = x_i_0[:]
    x_iii = x_i_0[:]
    k = 0
    step = 0
    while 1:
        # step 0 - exploratory search (part of iteration of the coordinate descent method)
        if step == 0:
            k += 1
            if k == 1:
                f = lambda x1: np.sqrt(pow(x1, 2) + 4) + np.sqrt(pow((x_i_0[1] - x1), 2) + 16) + np.sqrt(pow((x_i_0[1] - 5), 2) + 9)
                res = fmin(f, x_i_0[0], disp=False)
                x_i[0] = res[0]
                optimizations += 1
            if k == 2:
                f = lambda x2: np.sqrt(pow(x_i[0], 2) + 4) + np.sqrt(pow((x2 - x_i[0]), 2) + 16) + np.sqrt(pow((x2 - 5), 2) + 9)
                res = fmin(f, x_i_0[1], disp=False)
                x_i[1] = res[0]
                optimizations += 1
            for i in range(len(e_i)):
                e_i[i] = abs(x_i[i] - x_i_0[i])
            if k < n:
                continue
            else:
                step = 1
                print(f"iter = {iterations}\n\tx01 = {x_i_0[0]}\tx02 = {x_i_0[1]}\n\tx1 = {x_i[0]}\tx2 = {x_i[1]}\n\toptimizations = {optimizations}")
                optimizations = 0
        if step == 1:
            # step 1 - pattern search (part of iteration of the Hooke-Jeeves method)
            iterations += 1
            f = lambda b: np.sqrt(pow((x_i[0] + b * (x_i[0] - x_i_0[0])), 2) + 4) + np.sqrt(
                pow(((x_i[1] + b * (x_i[1] - x_i_0[1])) - (x_i[0] + b * (x_i[0] - x_i_0[0]))), 2) + 16) + np.sqrt(
                pow(((x_i[1] + b * (x_i[1] - x_i_0[1])) - 5), 2) + 9)
            optimizations += 1
            res = fmin(f, x_i[0], disp=False)
            temp = res[0]
            x_ii[0] = x_i[0] + temp * (x_i[0] - x_i_0[0])
            x_ii[1] = x_i[1] + temp * (x_i[1] - x_i_0[1])
            print(f"iter = {iterations}\n\tx01 = {x_i_0[0]}\tx02 = {x_i_0[1]}\n\tx1 = {x_i[0]}\tx2 = {x_i[1]}\n\tx11 = {x_ii[0]}\tx22 = {x_ii[1]}\n\toptimizations = {optimizations}")
            optimizations = 0

            # step 2 - optimization in the perpendicular direction (Rosenbrock)
            iterations += 1
            f = lambda b: np.sqrt(pow((x_ii[0] + b * (x_i[1] - x_i_0[1])), 2) + 4) + np.sqrt(
                pow(((x_ii[1] + b * (x_i[0] - x_i_0[0])) - (x_ii[0] + b * (x_i[1] - x_i_0[1]))), 2) + 16) + np.sqrt(
                pow(((x_ii[1] + b * (x_i[0] - x_i_0[0])) - 5), 2) + 9)
            optimizations += 1
            res = fmin(f, x_i[0], disp=False)
            temp = res[0]
            x_iii[0] = x_ii[0] + temp * (x_i[1] - x_i_0[1])
            x_iii[1] = x_ii[1] + temp * (x_i[0] - x_i_0[0])
            print(
                f"iter = {iterations}\n\tx01 = {x_i_0[0]}\tx02 = {x_i_0[1]}\n\tx1 = {x_i[0]}\tx2 = {x_i[1]}\n\tx11 = "
                f"{x_ii[0]}\tx22 = {x_ii[1]}\n\tx111 = {x_iii[0]}\tx222 = {x_iii[1]}\n\toptimizations = {optimizations}")
            optimizations = 0

            # step 3
            for i in range(len(e_i)):
                e_i[i] = abs(x_iii[i] - x_i[i])
            for i in range(len(e_i)):
                if e_i[i] < e:
                    flag += 1
            if flag == 2:
                x_min = x_iii
                break
            else:
                x_i_0 = x_i[:]
                x_i = x_iii[:]
                flag = 0

    print(x_min)
    t2 = time.time() - t1
    print(f"\tExecution time = {t2} seconds")
    plt.show()
