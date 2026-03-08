---
name: sim-to-real-transfer
version: 1.0.0
description: Bridge simulation to real hardware. Domain randomization, system ID, hardware abstraction.
---

# Sim-to-Real Transfer

## Domain Randomization
- **Visual**: texture, lighting, camera pose, background
- **Dynamics**: friction, mass, damping, actuator delay
- **Observation noise**: Gaussian noise on sensors, dropout
- **Action**: smoothing, latency simulation (1-3 step delay)

## Strategies
| Approach | When | Pros | Cons |
|----------|------|------|------|
| Domain randomization | No real data | Simple, scalable | Over-conservative |
| System identification | Some real data | Accurate | Requires instrumentation |
| Fine-tuning in real | After sim training | Best performance | Needs safe exploration |
| Asymmetric actor-critic | Privileged sim info | Uses GT in training only | Complex implementation |

## Hardware Abstraction
Design interfaces that work identically in sim and real:
```python
class RobotInterface(ABC):
    def get_observation(self) -> dict: ...
    def send_action(self, action: np.ndarray) -> None: ...
    def reset(self) -> dict: ...
```

## Key Libraries
Isaac Sim/Lab, MuJoCo, Gazebo, PyBullet
