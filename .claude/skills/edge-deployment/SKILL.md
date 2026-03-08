---
name: edge-deployment
description: Deploy ML models on edge hardware. Runtime selection, containerized edge, OTA updates, MQTT telemetry.
---

# Edge Deployment

## Runtime Selection
| Hardware | Runtime | Format |
|----------|---------|--------|
| Jetson (NVIDIA) | TensorRT | .engine |
| Mobile (ARM) | TFLite | .tflite |
| Intel CPU/GPU | OpenVINO | .xml/.bin |
| Apple Silicon | CoreML | .mlmodel |
| Any CPU | ONNX Runtime | .onnx |

## Containerized Edge
```dockerfile
FROM nvcr.io/nvidia/l4t-tensorrt:r8.5.2-runtime
COPY model.engine /models/
COPY app.py /app/
CMD ["python", "/app/app.py"]
```
Use K3s for orchestration, Balena for fleet management.

## OTA Model Updates
1. Version models with hash + timestamp
2. Download new model in background
3. Validate checksum, test inference on canary input
4. Atomic swap (symlink switch)
5. Rollback on failure

## Telemetry
MQTT for lightweight device-to-cloud: detections, health, metrics.

## Key Libraries
TensorRT, TFLite, ONNX Runtime, MQTT (mosquitto), AWS IoT Greengrass
