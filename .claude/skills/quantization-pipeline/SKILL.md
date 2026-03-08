---
name: quantization-pipeline
description: Model quantization for deployment. PTQ, QAT, INT8/FP16/INT4, hardware-specific calibration.
---

# Quantization Pipeline

## Post-Training Quantization (PTQ)
```python
from torch.quantization import quantize_dynamic
model_int8 = quantize_dynamic(model, {nn.Linear}, dtype=torch.qint8)
```

## TensorRT INT8
1. Prepare calibration dataset (100-1000 representative samples)
2. Choose calibration algorithm: entropy (default), minmax, percentile
3. Build engine with INT8 flag
4. Validate accuracy: target <1% degradation from FP32

## Methods Comparison
| Method | Bits | Needs Training | Best For |
|--------|------|---------------|----------|
| PTQ | 8 | No | Quick deployment |
| QAT | 8 | Yes | Max accuracy retention |
| GPTQ | 4 | No (calibration) | LLM serving |
| AWQ | 4 | No (calibration) | LLM serving |

## Validation
- Compare accuracy metrics (mAP, perplexity) vs full precision
- Measure latency speedup and memory reduction
- Test on edge cases (out-of-distribution inputs)

## Key Libraries
torch.quantization, TensorRT, OpenVINO, ONNX Runtime
