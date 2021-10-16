'''
метод покоординатного спуска (многомерная безусловная оптимизация)
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

if __name__ == "__main__":
    # построение графика функции
    x1, x2 = np.mgrid[0:5:0.01, 0:5:0.01]
    y = np.sqrt(pow(x1, 2) + 4) + np.sqrt(pow((x2 - x1), 2) + 16) + np.sqrt(pow((x2 - 5), 2) + 9)
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x1, x2, y, cmap="viridis")
    # метод покоординатного спуска
    A1 = A2 = 0
    B1 = B2 = 5
    e = 0.001
    plt.show()
