---
name: ml-testing
version: 1.0.0
description: ML-specific testing. Shape validation, gradient flow, convergence sanity, data pipeline determinism.
---

# ML Testing

## Model Tests
```python
def test_forward_pass():
    model = MyModel()
    x = torch.randn(2, 3, 224, 224)
    out = model(x)
    assert out.shape == (2, num_classes)
    assert not torch.isnan(out).any()

def test_gradient_flow():
    model = MyModel()
    x = torch.randn(2, 3, 224, 224, requires_grad=True)
    loss = model(x).sum()
    loss.backward()
    for name, p in model.named_parameters():
        assert p.grad is not None, f"No gradient for {name}"
        assert not torch.isnan(p.grad).any()
```

## Training Sanity
- Overfit on 1 batch: loss should -> 0
- Training loss should decrease monotonically (early epochs)
- Validation metrics should improve then plateau

## Data Pipeline Tests
- Determinism: same seed -> same batch
- Augmentation: output shapes/types unchanged
- No data leakage between train/val/test splits

## Regression Tests
- Track key metrics per commit (mAP, accuracy, latency)
- Alert on >1% degradation

## Key Libraries
pytest, torchtest, great_expectations
