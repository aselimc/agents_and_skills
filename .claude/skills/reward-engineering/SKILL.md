---
name: reward-engineering
version: 1.0.0
description: Design reward functions. Dense shaping, normalization, curriculum, and common pitfalls.
---

# Reward Engineering

## Design Principles
1. **Dense > Sparse**: provide gradient signal at every step
2. **Decompose**: `r = w1*r_task + w2*r_safety + w3*r_energy`
3. **Normalize**: running mean/std normalization of returns
4. **Potential-based shaping**: `F(s,s') = gamma*phi(s') - phi(s)` preserves optimal policy

## Common Pitfalls
- **Reward hacking**: agent finds unintended shortcuts (e.g., spinning to accumulate velocity reward)
- **Magnitude imbalance**: one term dominates, others are ignored
- **Sparse trap**: agent never discovers reward, learns nothing
- **Sign confusion**: mixing positive rewards and penalties without clear accounting

## Curriculum-Based Rewards
- Start with generous shaping, gradually reduce
- Success thresholds: advance difficulty when success_rate > 0.8
- Task difficulty: vary object size, target distance, terrain complexity

## Learned Rewards
- **IRL**: learn from demonstrations
- **RLHF**: learn from human preferences
- **Success classifiers**: binary reward from learned classifier

## Key Libraries
gymnasium, Isaac Lab
