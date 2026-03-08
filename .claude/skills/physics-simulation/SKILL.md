---
name: physics-simulation
description: Physics engine patterns. Rigid body dynamics, collision detection, constraint solvers, determinism.
---

# Physics Simulation

## Core Components
1. **Broad phase**: spatial partitioning (BVH, spatial hashing) to find candidate pairs
2. **Narrow phase**: exact collision (GJK, SAT) + contact manifold generation
3. **Solver**: resolve constraints (sequential impulse, PGS)
4. **Integration**: update positions/velocities (semi-implicit Euler, Verlet)

## Determinism
- Fixed timestep: `dt = 1/240` (never use variable dt for ML training)
- State snapshotting for replay/debugging
- Deterministic floating-point: same hardware + same order of operations

## ML Integration
- Gym/Gymnasium wrapper around simulation step
- Parallel envs: Isaac Gym (GPU), vectorized MuJoCo
- Reward computed from simulation state (contacts, distances, velocities)

## Common Engines
| Engine | Best For | Language |
|--------|----------|---------|
| MuJoCo | Research, contact-rich | C/Python |
| Isaac Sim/Lab | GPU-parallel RL | Python |
| PyBullet | Quick prototyping | Python |
| PhysX | Real-time, games | C++ |
| Gazebo | ROS integration | C++ |

## Key Libraries
MuJoCo, PyBullet, Isaac Sim, PhysX, Gazebo
