from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x ** 2 - y ** 2

#create 3d axes
fig = plt.figure()
# строим поверхность
ax = plt.axes(projection='3d')
ax.set_title('Поверхность F(x, y) = x^2 - y^2') 
x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)

x_list = list(np.linspace(-10, 10, 10))
y_list = list(np.linspace(-10, 10, 10))

X, Y = np.meshgrid(x, y)

Z = f(X, Y)

ax.contour3D(X, Y, Z, 100)

plt.show()

# # строим поле направлений

plt.quiver(X, Y, X / np.sqrt(X**2 + Y**2), -Y / np.sqrt(X**2 + Y**2), color='pink')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Поле направлений F(x, y) = x^2 - y^2')
plt.show()