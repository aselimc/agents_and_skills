---
name: sensor-fusion-pipeline
version: 1.0.0
description: Multi-sensor fusion. EKF/UKF state estimation, camera-LiDAR-IMU calibration, point cloud registration.
---

# Sensor Fusion Pipeline

## EKF State Estimation (robot_localization)
```yaml
# ekf.yaml
frequency: 50.0
odom0: /wheel_odom
odom0_config: [true, true, false, false, false, true, ...]
imu0: /imu/data
imu0_config: [false, false, false, true, true, true, ...]
```

## Calibration
- **Camera-LiDAR**: extrinsic calibration with checkerboard or targetless methods
- **Camera-IMU**: use kalibr for spatiotemporal calibration
- **Hand-eye**: AX=XB solvers (OpenCV, easy_handeye)

## Point Cloud Registration
```python
import open3d as o3d
result = o3d.pipelines.registration.registration_icp(
    source, target, max_distance=0.05,
    estimation_method=o3d.pipelines.registration.TransformationEstimationPointToPlane())
```

## Key Libraries
robot_localization, Open3D, kalibr, kiss-icp
