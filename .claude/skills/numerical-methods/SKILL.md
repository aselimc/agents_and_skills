---
name: numerical-methods
description: Numerical solvers. ODE/PDE, FEM, sparse linear algebra, stability analysis.
---

# Numerical Methods

## ODE Solvers
```python
from scipy.integrate import solve_ivp
sol = solve_ivp(rhs, [0, 10], y0, method='RK45', rtol=1e-8)
# For stiff systems: method='Radau' or 'BDF'
```

## PDE / FEM
```python
# FEniCS
from fenics import *
mesh = UnitSquareMesh(32, 32)
V = FunctionSpace(mesh, 'P', 1)
u = TrialFunction(V); v = TestFunction(V)
a = dot(grad(u), grad(v)) * dx
L = f * v * dx
solve(a == L, u_h, bc)
```

## Sparse Linear Algebra
- Direct: LU/Cholesky for small-medium systems (<10^5 unknowns)
- Iterative: CG (SPD), GMRES (general) with AMG preconditioner for large systems
- Format: CSR for arithmetic, COO for construction

## Stability
- CFL condition for explicit time-stepping: `dt < dx / c`
- Stiffness detection: large ratio of eigenvalues -> use implicit solver

## Key Libraries
SciPy, JAX, FEniCS, PETSc, Julia DifferentialEquations.jl
