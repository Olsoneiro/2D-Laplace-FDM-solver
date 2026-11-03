import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return 0.5 * np.log(x**2 + y**2)

def fdm(N):
    a = 1
    w0 = 1
    x = np.linspace(w0, w0 + a, N)
    y = np.linspace(w0, w0 + a, N)
    X, Y = np.meshgrid(x, y)

    analytical = f(X, Y)

    u = np.zeros((N, N))
    u = np.array(u)

    bottom = 0.5 * np.log(x**2 + 1)
    top = 0.5 * np.log(x**2 + 4)
    left = 0.5 * np.log(1 + y**2)
    right = 0.5 * np.log(4 + y**2)

    u[0, :] = bottom
    u[N-1, :] = top
    u[:, 0] = left
    u[:, N-1] = right

    max_iter = 100000

    for iteration in range(1, max_iter + 1):
        u[1:N-1, 1:N-1] = 0.25 * (u[2:, 1:N-1] + u[:N-2, 1:N-1] + u[1:N-1, 2:] + u[1:N-1, :N-2])

        # Calculate maximum error relative to the exact analytical solution
        error = np.abs(u - analytical)

        if iteration % 500 == 0:
            plt.scatter(X, error)
            plt.xlabel('X')
            plt.ylabel('Error')

        if np.max(error) <= 1e-4:
            break

    return X, Y, u, analytical, iteration, error

grids = [10, 25, 50, 75, 100]
print('Grid | Iterations | Max Error')
for N in grids:
    X, Y, u, analytical, iteration, error = fdm(N)
    print(f"{N}x{N} | {iteration} | {np.max(error)}")

fig = plt.figure(figsize=(16, 6))

ax1 = fig.add_subplot(1, 3, 1, projection='3d')
surf1 = ax1.plot_surface(X, Y, u, cmap='viridis')
ax1.set_title(f'Numerical Solution (N={N})')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)

ax2 = fig.add_subplot(1, 3, 2, projection='3d')
surf2 = ax2.plot_surface(X, Y, analytical, cmap='plasma')
ax2.set_title('Analytical Solution')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)

ax3 = fig.add_subplot(1, 3, 3)
error_map = np.abs(u - analytical)
img = ax3.contourf(X, Y, error_map, levels=50, cmap='turbo')
ax3.set_title('Error Map |Numerical - Analytical|')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
fig.colorbar(img, ax=ax3)

fig2 = plt.figure(figsize=(14, 6))
ax4 = fig2.add_subplot(1, 2, 1)
img_num = ax4.contourf(X, Y, u, levels=50, cmap='viridis')
ax4.set_title(f'Numerical Solution (N={N})')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
fig2.colorbar(img_num, ax=ax4)

ax5 = fig2.add_subplot(1, 2, 2)
img_an = ax5.contourf(X, Y, analytical, cmap='plasma')
ax5.set_title('2D Analytical Solution')
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
fig2.colorbar(img_an, ax=ax5)

plt.tight_layout()
plt.show()
