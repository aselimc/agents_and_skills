---
name: llm-finetuning
version: 1.0.0
description: Fine-tune LLMs with LoRA/QLoRA, instruction tuning, and alignment (DPO/ORPO).
---

# LLM Fine-Tuning

## LoRA/QLoRA (Parameter-Efficient)
```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=16, lora_alpha=32, target_modules=["q_proj", "v_proj"],
                    lora_dropout=0.05, task_type="CAUSAL_LM")
model = get_peft_model(model, config)
```

## Data Formats
- **Alpaca**: `{"instruction": ..., "input": ..., "output": ...}`
- **ShareGPT**: `{"conversations": [{"from": "human", "value": ...}, ...]}`
- **OpenAI**: `{"messages": [{"role": "user", "content": ...}, ...]}`

## Alignment
- **DPO**: direct preference optimization, no reward model needed
- **ORPO**: odds ratio preference, single-stage
- **SimPO**: simple preference optimization with reference-free margin

## Memory Optimization
- Gradient checkpointing: `model.gradient_checkpointing_enable()`
- DeepSpeed ZeRO Stage 2/3 for multi-GPU
- QLoRA: 4-bit base model + LoRA adapters

## Evaluation
Perplexity, downstream benchmarks, MT-Bench/AlpacaEval, human eval

## Key Libraries
transformers, trl, peft, unsloth, axolotl
