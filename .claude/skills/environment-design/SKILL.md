---
name: environment-design
description: RL environment design. Gymnasium API, vectorized envs, observation/action spaces, curriculum.
---

# Environment Design

## Gymnasium API
```python
class MyEnv(gymnasium.Env):
    def __init__(self):
        self.observation_space = spaces.Box(-np.inf, np.inf, shape=(obs_dim,))
        self.action_space = spaces.Box(-1, 1, shape=(act_dim,))
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        return obs, info
    def step(self, action):
        return obs, reward, terminated, truncated, info
```

## Vectorized Environments
```python
envs = gymnasium.make_vec("MyEnv-v0", num_envs=16,
    vectorization_mode="async")  # SubprocVecEnv equivalent
```
For GPU: Isaac Gym/Lab provides thousands of parallel envs on GPU.

## Observation Design
- Normalize to roughly [-1, 1] range
- Include relevant history if partially observable
- Proprioception: joint positions/velocities normalized by limits
- Use depth over RGB when possible (transfers better)

## Curriculum
- Terrain difficulty: flat -> slopes -> stairs -> rough
- Task complexity: reach -> grasp -> place -> manipulate
- Advance when success_rate > threshold (e.g., 0.8)

## Key Libraries
gymnasium, Isaac Gym/Lab, PettingZoo, dm_control
