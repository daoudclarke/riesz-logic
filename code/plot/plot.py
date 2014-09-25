from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from itertools import product

def get_func_values(f):
    x_range = y_range = np.arange(0.0, 1.0, 0.005)
    X, Y = np.meshgrid(x_range, y_range)
    #Z = np.zeros((100,100))
    # for i, x in enumerate(X[0,:]):
    #     for j, y in enumerate(Y[:,0]):
    #         Z[i, j] = f(x, y)
    Z = f(X,Y)
    return X, Y, Z

def plot(values):
    X, Y, Z = values
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
    cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

    ax.set_xlabel('X')
    ax.set_xlim(0, 1)
    ax.set_ylabel('Y')
    ax.set_ylim(0, 1)
    ax.set_zlabel('Z')
    ax.set_zlim(0., 1.)

    #ax = Axes3D(fig)
    ax.view_init(elev=45., azim=225)
    #plt.show()
    
    plt.savefig("lukasiewicz.svg", transparent=True)

def logistic_add(x, y):
    return x*y/(1 - x - y + 2*x*y)

def lukasiewicz(x, y):
    return np.maximum(0, x + y - 1)

if __name__ == "__main__":
    values = get_func_values(lukasiewicz)
    #values = get_func_values(logistic_add)
    #values = np.nan_to_num(values)
    #values = get_func_values(lambda x, y: x+y)
    #print [x.shape for x in values]
    plot(values)
