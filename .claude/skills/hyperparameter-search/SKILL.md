---
name: hyperparameter-search
description: Systematic hyperparameter optimization with Optuna. Bayesian search with pruning.
---

# Hyperparameter Search

## Optuna Pattern
```python
import optuna

def objective(trial):
    lr = trial.suggest_float("lr", 1e-5, 1e-2, log=True)
    bs = trial.suggest_categorical("batch_size", [16, 32, 64])
    wd = trial.suggest_float("weight_decay", 1e-6, 1e-2, log=True)

    model = build_model(trial)
    val_metric = train_and_eval(model, lr, bs, wd)

    trial.report(val_metric, step=epoch)  # for pruning
    if trial.should_prune(): raise optuna.TrialPruned()
    return val_metric

study = optuna.create_study(direction="maximize",
    pruner=optuna.pruners.MedianPruner(n_warmup_steps=5))
study.optimize(objective, n_trials=100)
print(study.best_params)
```

## Rules
- Use log-uniform for learning rates
- Use categorical for architecture choices
- Enable pruning (MedianPruner) to save compute
- Report best config reproducibly (save full config, not just best params)
- For multi-objective (accuracy vs latency): `create_study(directions=["maximize", "minimize"])`

## Key Libraries
optuna, ray[tune]
