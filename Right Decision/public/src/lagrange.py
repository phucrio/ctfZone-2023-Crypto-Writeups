import numpy as np
import matplotlib.pyplot as plt


class LagrangePoly:

    def __init__(self, X, Y):
        self.n = len(X)
        self.X = np.array(X)
        self.Y = np.array(Y)

    def basis(self, x, j):
        b = [(x - self.X[m]) / (self.X[j] - self.X[m])
             for m in range(self.n) if m != j]
        return np.prod(b, axis=0) * self.Y[j]

    def interpolate(self, x):
        b = [self.basis(x, j) for j in range(self.n)]
        return np.sum(b, axis=0)


X  = [1, 2, 3, 4,5]
Y  = [44, 298, 1230, 3266,6822]

plt.scatter(X, Y, c='k')

lp = LagrangePoly(X, Y)

xx = np.arange(-100, 100) / 10

plt.plot(xx, lp.basis(xx, 0))
plt.plot(xx, lp.basis(xx, 1))
plt.plot(xx, lp.basis(xx, 4))
plt.plot(xx, lp.basis(xx, 3))
plt.plot(xx, lp.interpolate(xx), linestyle=':')
plt.show()