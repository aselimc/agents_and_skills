---
name: high-performance-computing
version: 1.0.0
description: Performance optimization. Vectorization, memory layout, GPU acceleration, profiling, parallelism.
---

# High-Performance Computing

## Profiling First
```bash
# Python
python -m cProfile -o prof.out script.py
py-spy record -o profile.svg -- python script.py
# GPU
nsight systems profile python train.py
```

## Vectorization
- Replace Python loops with NumPy/JAX operations
- Use `jax.jit` for JIT compilation of pure functions
- Batch operations: process N items at once, not one-by-one

## Memory Layout
- AoS (Array of Structs) vs SoA (Struct of Arrays): SoA for SIMD/GPU
- Contiguous memory: `np.ascontiguousarray()`, `tensor.contiguous()`
- Avoid unnecessary copies: use views, in-place operations

## GPU Acceleration
```python
import jax
@jax.jit
def compute(x): return jax.numpy.dot(x, x.T)
```
Or Numba for CUDA kernels, CuPy for drop-in NumPy replacement.

## Parallelism
- `multiprocessing.Pool` for CPU-bound
- `joblib.Parallel` for embarrassingly parallel
- `torch.distributed` for multi-GPU training

## Key Libraries
JAX, NumPy, Numba, CuPy, line_profiler
