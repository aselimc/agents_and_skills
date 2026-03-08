---
name: motion-planning-control
description: Motion planning and control. MoveIt2, Nav2, trajectory optimization, PID/MPC, ros2_control.
---

# Motion Planning & Control

## MoveIt2 (Manipulation)
- Configure SRDF, kinematics (KDL/TRAC-IK), collision objects
- Planners: OMPL (RRT*, PRM*), PILZ (industrial), STOMP
- Use MoveGroup interface for planning + execution

## Nav2 (Mobile Navigation)
- Planners: NavFn, Theta*, Smac (lattice/hybrid A*)
- Controllers: DWB, MPPI, regulated pure pursuit
- Costmaps: static + obstacle + inflation layers

## Control Loops
| Controller | Use Case | Tuning |
|-----------|----------|--------|
| PID | Joint position/velocity | Ziegler-Nichols or manual |
| MPC | Trajectory tracking with constraints | Horizon, Q, R matrices |
| Impedance | Compliant manipulation | Stiffness, damping |

## ros2_control
```yaml
hardware:
  - hardware_interface/JointStateInterface
  - hardware_interface/EffortJointInterface
controllers:
  joint_trajectory_controller:
    type: joint_trajectory_controller/JointTrajectoryController
```

## Key Libraries
MoveIt2, Nav2, ros2_control, Drake, pinocchio
