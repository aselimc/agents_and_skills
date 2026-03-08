---
name: rl-algorithm-implementation
version: 1.0.0
description: Implement RL algorithms (PPO, SAC, TD3) with proper numerical stability and vectorized envs.
---

# RL Algorithm Implementation

## PPO Essentials
- GAE for advantage estimation (lambda=0.95, gamma=0.99)
- Clip ratio 0.2, entropy coefficient 0.01
- Value function clipping (optional, debated)
- Orthogonal initialization, layer norm optional
- Observation normalization (RunningMeanStd)

## SAC Essentials
- Twin Q-networks, separate target networks (tau=0.005)
- Auto-tuned temperature alpha (target entropy = -dim(action))
- No target for policy network
- Replay buffer size: 1M typical

## TD3 Essentials
- Delayed policy updates (every 2 critic updates)
- Target policy smoothing (noise clip 0.5)
- Twin Q minimum for target

## Common Infrastructure
```python
# Observation normalization
class RunningMeanStd:
    def update(self, x): ...
    def normalize(self, x): return (x - self.mean) / (self.var + 1e-8).sqrt()
```

## Debugging Checklist
1. Check reward scale and normalization
2. Monitor policy entropy (should decrease gradually)
3. Watch Q-value magnitudes (divergence = bug)
4. Verify gradient norms
5. Sanity test on CartPole/Pendulum first

## Key Libraries
CleanRL, Stable-Baselines3, TorchRL, gymnasium
