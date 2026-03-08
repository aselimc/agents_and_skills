---
name: experiment-tracking
version: 1.0.0
description: Track ML experiments with W&B or MLflow. Log hyperparams, metrics, artifacts, and system metrics.
---

# Experiment Tracking

## W&B (Preferred)
```python
import wandb
wandb.init(project="my-project", config=cfg, tags=["baseline"])
wandb.log({"train/loss": loss, "train/lr": lr, "epoch": epoch})
wandb.log({"val/mAP": map_score})
wandb.save("checkpoints/best.pt")
wandb.finish()
```

## MLflow
```python
import mlflow
mlflow.set_experiment("my-experiment")
with mlflow.start_run():
    mlflow.log_params(cfg)
    mlflow.log_metric("val_loss", val_loss, step=epoch)
    mlflow.log_artifact("checkpoints/best.pt")
```

## What to Log
- **Always**: hyperparams, train/val metrics per epoch, LR schedule, git commit hash, full config
- **System**: GPU utilization, memory usage, throughput (samples/sec)
- **Artifacts**: best checkpoint, config YAML, sample predictions
- **Tags**: experiment name, model variant, dataset version

## Rules
- Group runs by experiment, tag for filtering
- Log config diff from baseline for quick comparison
- Use run names that encode key hyperparams (e.g., `lr1e-4_bs32_ep100`)
