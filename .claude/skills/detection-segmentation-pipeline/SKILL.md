---
name: detection-segmentation-pipeline
version: 1.0.0
description: Object detection and segmentation pipelines. COCO/VOC formats, DETR/YOLO/Mask2Former, mAP/mIoU evaluation.
---

# Detection & Segmentation Pipeline

## Data Formats
- **COCO**: JSON annotations, `[x, y, w, h]` bbox format
- **VOC**: XML per image, `[xmin, ymin, xmax, ymax]`
- **YOLO**: txt per image, `[class cx cy w h]` normalized

## Model Selection
| Task | Recommended | Alternative |
|------|------------|-------------|
| 2D Detection | RT-DETR, YOLOv8 | Faster R-CNN, DINO |
| Instance Seg | Mask2Former | Mask R-CNN |
| Semantic Seg | SegFormer, Mask2Former | DeepLabv3+ |
| Panoptic | Mask2Former | - |
| 3D Detection | CenterPoint, PointPillars | VoxelNet |

## Evaluation
- Detection: COCO mAP (AP@0.5, AP@0.5:0.95, AP_S/M/L)
- Segmentation: mIoU, per-class IoU, boundary F1
- Always report FLOPs and inference latency alongside accuracy

## Key Libraries
mmdetection, detectron2, ultralytics, torchvision
