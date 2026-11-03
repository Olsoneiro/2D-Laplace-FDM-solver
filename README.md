# 2D Laplace Equation Solver — Finite Difference Method (FDM)

A Python implementation of the **Finite Difference Method (FDM)** for solving the two-dimensional Laplace equation on a square domain, complete with convergence benchmarking across multiple grid resolutions and 2D/3D visualizations comparing the numerical approximation against the exact analytical solution.

## Problem Formulation

This script solves the 2D Laplace equation:

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

over the square domain $(x, y) \in [1, 2] \times [1, 2]$.

### Analytical Solution & Boundary Conditions

The exact analytical solution used for boundary assignment and error verification is the harmonic function:

$$u(x, y) = \frac{1}{2} \ln(x^2 + y^2)$$

Dirichlet boundary conditions are applied along the four edges of the domain:
* **Bottom ($y = 1$):** $u(x, 1) = 0.5 \ln(x^2 + 1)$
* **Top ($y = 2$):** $u(x, 2) = 0.5 \ln(x^2 + 4)$
* **Left ($x = 1$):** $u(1, y) = 0.5 \ln(1 + y^2)$
* **Right ($x = 2$):** $u(2, y) = 0.5 \ln(4 + y^2)$

### Numerical Scheme

The interior nodes of the $N \times N$ uniform grid are updated iteratively using the 5-point stencil average:

$$u_{i,j}^{(k+1)} = \frac{1}{4} \left( u_{i+1,j}^{(k)} + u_{i-1,j}^{(k)} + u_{i,j+1}^{(k)} + u_{i,j-1}^{(k)} \right)$$

Iterations continue until the maximum absolute error satisfies:

$$\max \vert{}u_{\text{numerical}} - u_{\text{analytical}}\vert{} \le 10^{-4}$$

or until the limit of `100,000` iterations is reached.

## Features

* **Multi-Grid Benchmarking:** Evaluates convergence speed and accuracy across five grid resolutions ($10\times10$, $25\times25$, $50\times50$, $75\times75$, and $100\times100$).
* **3D Surface Plots:** Side-by-side 3D surface comparison of the numerical and analytical solutions for $N=100$.
* **2D Contour & Error Heatmaps:** High-resolution contour maps of both solutions and the spatial distribution of absolute error $\vert{}u_{\text{num}} - u_{\text{exact}}\vert{}$.

## Requirements

* Python 3.8+
* `numpy`
* `matplotlib`

Install the dependencies via `pip`:

```bash
pip install numpy matplotlib
```

## Usage

Run the script directly from the terminal:

```bash
python run.py
```

### Sample Console Output

The console outputs a summary table showing the number of iterations required to reach the target tolerance for each grid size:

```text
Grid | Iterations | Max Error
10x10 | ... | ...
25x25 | ... | ...
50x50 | ... | ...
75x75 | ... | ...
100x100 | ... | ...
```