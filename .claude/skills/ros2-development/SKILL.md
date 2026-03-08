---
name: ros2-development
version: 1.0.0
description: Idiomatic ROS2 development. Lifecycle nodes, QoS, launch files, TF2, custom messages.
---

# ROS2 Development

## Node Pattern (rclpy)
```python
class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.sub = self.create_subscription(LaserScan, 'scan', self.scan_cb,
            QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT, depth=5))
        self.timer = self.create_timer(0.1, self.timer_cb)
```

## QoS Cheat Sheet
- Sensors: `BEST_EFFORT`, `VOLATILE`, depth=5
- Commands: `RELIABLE`, `VOLATILE`, depth=10
- Map data: `RELIABLE`, `TRANSIENT_LOCAL`, depth=1

## Standards
- REP-103: SI units (meters, radians, seconds)
- REP-105: frame names (base_link, odom, map)
- Use `sim_time` in simulation, `wall_time` on real hardware
- Lifecycle nodes for managed startup/shutdown

## Key Libraries
rclpy, rclcpp, launch_ros, tf2_ros, robot_state_publisher
