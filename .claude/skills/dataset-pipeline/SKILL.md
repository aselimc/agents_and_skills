---
name: dataset-pipeline
description: PyTorch Dataset/DataLoader patterns for efficient, reproducible data loading and augmentation.
---

# Dataset Pipeline

## Standard Pattern
```python
class MyDataset(Dataset):
    def __init__(self, root, split, transform=None):
        self.samples = self._load_manifest(root, split)
        self.transform = transform
    def __len__(self): return len(self.samples)
    def __getitem__(self, idx):
        img, label = self._load_sample(self.samples[idx])
        if self.transform: img = self.transform(img)
        return img, label
```

## DataLoader Config
```python
DataLoader(dataset, batch_size=32, shuffle=True, num_workers=8,
           pin_memory=True, prefetch_factor=2, persistent_workers=True)
```

## Augmentation
- **CV**: albumentations or torchvision.transforms.v2
- **NLP**: tokenizer pipelines (HuggingFace tokenizers)
- **Audio**: torchaudio.transforms

## Rules
- Reproducible splits: seeded RNG, save split indices
- Validate data at load time (check shapes, dtypes, NaN)
- Use memory-mapped formats for large datasets (webdataset, HF datasets)
- Never augment validation/test data (except TTA at inference)

## Key Libraries
torch.utils.data, albumentations, torchvision.transforms, HuggingFace datasets, webdataset
