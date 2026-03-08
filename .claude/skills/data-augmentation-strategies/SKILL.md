---
name: data-augmentation-strategies
description: Domain-appropriate data augmentation for CV, robotics, and NLP pipelines.
---

# Data Augmentation Strategies

## CV Augmentation (albumentations)
```python
import albumentations as A
transform = A.Compose([
    A.RandomResizedCrop(224, 224, scale=(0.2, 1.0)),
    A.HorizontalFlip(p=0.5),
    A.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.2, hue=0.1),
    A.GaussianBlur(blur_limit=(3, 7), p=0.5),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2(),
])
```

## Mixing Strategies
- **CutMix**: replace random patch with another image's patch + mix labels
- **MixUp**: linear interpolation of images and labels
- **Mosaic**: 4 images in quadrants (YOLO-style)

## Domain-Specific
- **Medical**: intensity windowing, elastic deformation, no flips if laterality matters
- **Satellite**: full rotation invariance, multi-scale crops
- **Robotics**: viewpoint synthesis, lighting variation, background randomization

## Rules
- Never augment validation/test sets (except TTA at inference)
- Visually inspect augmented samples before training
- Match augmentation strength to dataset size (stronger for small datasets)

## Key Libraries
albumentations, torchvision.transforms.v2, kornia
