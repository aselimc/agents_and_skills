---
name: world-model-implementation
description: Learned dynamics models for prediction and planning. RSSM, JEPA, Dreamer, imagination-based RL.
---

# World Model Implementation

## Architecture Families
| Family | Key Model | Latent Space | Best For |
|--------|----------|-------------|----------|
| RSSM | Dreamer v3 | Discrete categorical | Model-based RL, control |
| Transformer | IRIS, STORM | Discrete tokens (VQ) | Long-horizon prediction |
| JEPA | I-JEPA, V-JEPA | Continuous embeddings | Representation pretraining |
| Diffusion | Video diffusion | Continuous | High-quality prediction |

## RSSM Core
```python
# Dreamer-style recurrent state-space model
h_t = GRU(h_{t-1}, z_{t-1}, a_{t-1})      # deterministic
z_t ~ posterior(h_t, x_t)                    # with observation
z_t_hat ~ prior(h_t)                        # without observation (imagination)
x_t_hat = decoder(h_t, z_t)                 # reconstruction
```

## Training Losses
- **Reconstruction**: MSE or perceptual loss for decoder
- **KL**: `KL(posterior || prior)` with free bits or KL balancing
- **Prediction**: latent-space prediction loss (JEPA-style)

## Evaluation
1. Short-horizon prediction accuracy (1-5 steps)
2. Long-horizon quality (FVD, LPIPS for video)
3. Downstream control performance (if model-based RL)
4. Representation quality (linear probe for JEPA)

## Imagination-Based Training (Dreamer)
```python
for imagination_step in range(horizon):
    action = actor(state)
    state = world_model.imagine(state, action)
    reward = reward_model(state)
    value = critic(state)
# Backprop through imagined trajectory to update actor
```

## Key Libraries
PyTorch, timm, MuJoCo, Isaac Lab, wandb
