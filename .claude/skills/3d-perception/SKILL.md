---
name: 3d-perception
description: 3D vision pipelines. Point clouds, depth estimation, 3D reconstruction, pose estimation, scene understanding.
---

# 3D Perception

## Point Cloud Processing
```python
import open3d as o3d
pcd = o3d.io.read_point_cloud("scene.ply")
pcd_down = pcd.voxel_down_sample(voxel_size=0.02)
pcd_down.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
```

## Core Tasks
| Task | Methods | Libraries |
|------|---------|-----------|
| Depth estimation | MiDaS, Depth Anything, stereo | torch, timm |
| 3D reconstruction | NeRF, 3DGS, TSDF fusion | nerfstudio, Open3D |
| 6DoF pose | FoundationPose, MegaPose | PyTorch3D |
| 3D segmentation | MinkowskiEngine, PTv3 | MinkowskiEngine |
| Scene graphs | 3DSSG, ConceptGraphs | custom |
| Registration | ICP, GICP, RANSAC | Open3D, kiss-icp |

## Coordinate Conventions
- ROS: X-forward, Y-left, Z-up (REP-103)
- OpenCV: X-right, Y-down, Z-forward
- OpenGL: X-right, Y-up, Z-backward
- Always document which convention is used

## Key Libraries
Open3D, PyTorch3D, kaolin, MinkowskiEngine, nerfstudio
