---
name: self-supervised-pretraining
description: Self-supervised visual representation learning. Contrastive, masked, distillation, and JEPA methods.
---

# Self-Supervised Pretraining

## Method Families
| Family | Methods | Key Mechanism |
|--------|---------|--------------|
| Contrastive | SimCLR, MoCo v3 | Positive/negative pairs, InfoNCE loss |
| Masked | MAE, BEiT | Reconstruct masked patches |
| Distillation | DINO, DINOv2 | EMA teacher, self-distillation |
| JEPA | I-JEPA, V-JEPA | Predict representations in latent space |

## Common Components
- **EMA teacher**: `teacher = momentum * teacher + (1 - momentum) * student`
- **Multi-crop**: 2 global views (224px) + N local views (96px)
- **Masking**: random/block masking with 60-80% mask ratio (MAE-style)
- **Collapse prevention**: centering, sharpening, stop-gradient

## Evaluation Protocol
1. **Linear probe**: freeze encoder, train linear classifier
2. **kNN**: k=20 nearest neighbors on frozen features
3. **Fine-tuning**: full or partial fine-tuning on downstream
4. Report on ImageNet-1k or domain-specific benchmark

## Key Libraries
timm, torchvision, lightly
