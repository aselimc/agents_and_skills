---
name: model-export-and-optimization
description: Export PyTorch models to ONNX/TensorRT for production deployment. Validate numerical equivalence.
---

# Model Export & Optimization

## PyTorch -> ONNX
```python
torch.onnx.export(model, dummy_input, "model.onnx",
    opset_version=17,
    input_names=["input"], output_names=["output"],
    dynamic_axes={"input": {0: "batch"}, "output": {0: "batch"}})
```

## ONNX -> TensorRT
```python
import tensorrt as trt
builder = trt.Builder(logger)
config = builder.create_builder_config()
config.set_flag(trt.BuilderFlag.FP16)  # or INT8
```

## Validation
```python
# Compare outputs
cos_sim = F.cosine_similarity(torch_out, onnx_out)
max_diff = (torch_out - onnx_out).abs().max()
assert cos_sim > 0.9999 and max_diff < 1e-3
```

## Checklist
1. Set model to `eval()` mode before export
2. Use correct opset version (17+ recommended)
3. Handle dynamic shapes (batch, sequence length)
4. Validate numerical equivalence on 100+ samples
5. Benchmark latency: PyTorch vs ONNX vs TensorRT

## Key Libraries
torch.onnx, onnxruntime, tensorrt, torch.jit
