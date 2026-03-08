---
name: paper-writing
version: 1.0.0
description: Academic paper writing. LaTeX, conference templates, experiment tables, rebuttals, contribution positioning.
---

# Paper Writing

## Paper Structure
1. **Abstract** (150-250 words): problem, gap, approach, results, significance
2. **Introduction** (~1.5p): hook, problem, limitations, contributions (numbered), outline
3. **Related Work** (~1p): thematic grouping, end each paragraph with differentiation
4. **Method** (~2-3p): notation, architecture, loss, training details
5. **Experiments** (~2-3p): setup, main results, ablations, analysis, failure cases
6. **Conclusion** (~0.5p): summary, limitations, future work

## LaTeX Essentials
- Tables: `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), bold best, underline 2nd
- Math: `\mathcal` for sets, `\mathbf` for vectors, `align` for multi-line
- Citations: `natbib` with `\citep{}` (parens) and `\citet{}` (textual)
- Figures: vector PDF for diagrams, self-contained captions

## Conference Templates
| Venue | Pages | Format | Key Rule |
|-------|-------|--------|----------|
| NeurIPS | 9 + unlimited appendix | Single column | `\usepackage[preprint]{neurips_2027}` for arxiv |
| ICML | 8 + unlimited appendix | Single column | - |
| CVPR/ICCV | 8 + refs + appendix | Two column | Double-blind |
| ICRA | 6-8 | IEEE two column | Include video link |

## Rebuttal
- Address every concern, even minor ones
- Structure: quote -> respond with evidence -> reference section/table
- Be respectful but firm on misunderstandings

## Key Libraries
LaTeX, booktabs, natbib, TikZ, matplotlib
