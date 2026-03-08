---
name: pytorch-training-pipeline
description: Standard PyTorch training patterns with AMP, DDP, checkpointing, and best practices.
---

# PyTorch Training Pipeline

## Standard Training Loop
```python
scaler = torch.amp.GradScaler()
for epoch in range(epochs):
    model.train()
    for batch in train_loader:
        optimizer.zero_grad()
        with torch.amp.autocast(device_type="cuda"):
            loss = model(batch)
        scaler.scale(loss).backward()
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        scaler.step(optimizer)
        scaler.update()
        scheduler.step()
```

## Checklist
1. **Sanity check**: overfit on 1 batch first
2. **AMP**: `torch.amp.autocast` + `GradScaler`
3. **Gradient clipping**: `clip_grad_norm_` (default 1.0)
4. **LR schedule**: cosine with warmup
5. **Checkpointing**: save model + optimizer + scheduler + epoch + best metric
6. **EMA**: optional but recommended for SSL/generative models
7. **Logging**: train/val loss, LR, grad norm per step
8. **Reproducibility**: `torch.manual_seed()`, `deterministic=True` for debugging

## Multi-GPU (DDP)
```python
model = DDP(model, device_ids=[local_rank])
sampler = DistributedSampler(dataset)
```

## Key Libraries
PyTorch, PyTorch Lightning, torchvision, timm
