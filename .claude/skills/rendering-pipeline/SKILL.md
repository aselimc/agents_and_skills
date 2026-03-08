---
name: rendering-pipeline
description: Rendering for simulation and synthetic data. PBR, domain randomization, depth/mask rendering.
---

# Rendering Pipeline

## Synthetic Data Generation
1. Randomize scene: object poses, textures, lighting, camera
2. Render: RGB + depth + normals + instance segmentation masks
3. Auto-generate annotations (bounding boxes, keypoints from mesh)

## Domain Randomization (Visual)
- Textures: random procedural, real-world texture datasets
- Lighting: HDR environment maps, point/area lights with random intensity
- Camera: intrinsics (focal length), extrinsics (pose), distortion
- Distractors: random objects in background

## Rendering Approaches
| Approach | Speed | Quality | Use Case |
|----------|-------|---------|----------|
| Rasterization (OpenGL) | Fast | Good | Real-time sim, large datasets |
| Ray tracing (OptiX) | Slow | Best | Photorealistic, small datasets |
| Neural rendering (NeRF/3DGS) | Medium | Good | View synthesis from real scenes |

## Performance
- LOD (Level of Detail) for distant objects
- Frustum/occlusion culling
- Instanced rendering for repeated objects
- Target: >30 FPS for real-time, batch rendering for offline

## Key Libraries
OpenGL, Vulkan, Unity, Unreal Engine, Blender (bpy)
