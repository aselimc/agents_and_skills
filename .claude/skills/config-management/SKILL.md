---
name: config-management
description: Config-driven design patterns. No hardcoded values in business logic.
---

# Config Management

## Python ML Projects
Use Hydra + OmegaConf:
```python
@hydra.main(config_path="configs", config_name="train")
def main(cfg: DictConfig):
    model = build_model(cfg.model)
    trainer = Trainer(**cfg.trainer)
```
Or dataclasses + env overrides:
```python
@dataclass
class TrainConfig:
    lr: float = 1e-4
    batch_size: int = 32
    epochs: int = 100
```

## Services (12-Factor)
- Config via environment variables
- Use `pydantic-settings` for typed env parsing
- `.env` files for local dev (always in `.gitignore`)
- Secrets via vault or cloud secret managers, never in config files

## Rules
- No magic numbers in code - all tunables in config
- Hierarchical: defaults < config file < env vars < CLI args
- Config must be serializable and reproducible
- Log the full config at startup for debugging
