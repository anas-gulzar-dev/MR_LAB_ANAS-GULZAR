# MCT-454L Mobile Robotics – Lab 2 Report
## ROS, Packages, Nodes, Topics, Services, RQT

---

## Steps Followed

### Step 1: Launching Turtlesim
- Sourced the ROS 2 environment using `source /opt/ros/humble/setup.bash`.
- Launched the Turtlesim node with:
  ```bash
  ros2 run turtlesim turtlesim_node
  ```
- A window appeared showing a turtle on a blue background.

### Step 2: Controlling the Turtle
- Opened a new terminal and ran the teleop node:
  ```bash
  ros2 run turtlesim turtle_teleop_key
  ```
- Used the keyboard arrow keys to move the turtle around the simulation window.

### Step 3: Exploring ROS 2 Topics
- Listed all active topics:
  ```bash
  ros2 topic list
  ```
- Echoed the turtle's position topic to observe real-time updates:
  ```bash
  ros2 topic echo /turtle1/pose
  ```
- Observed continuous position (x, y, theta) and velocity data being published as the turtle moved.

### Step 4: Sending Velocity Commands
- Published a velocity command directly to the turtle using:
  ```bash
  ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
  ```
- The turtle began moving in a circular arc as a result of the combined linear and angular velocity.

### Step 5: Resetting the Simulation
- Called the `/reset` service to return the turtle to its starting position:
  ```bash
  ros2 service call /reset std_srvs/srv/Empty
  ```
- The simulation cleared and the turtle reappeared at the center.

### Step 6: Using rqt
- Launched `rqt` and used the Plugins menu to explore the ROS 2 graph, topics, and services.
- Called the `/reset` service through the rqt Services GUI.
- Used the `/spawn` service to create a second turtle by setting `x`, `y`, `theta`, and a name.
- Identified `/turtle2/cmd_vel` as the topic for the second turtle and sent velocity commands to it, confirming that each turtle moves independently.

---

## Observations

- **Topics** allow nodes to communicate asynchronously by publishing and subscribing to named data streams. `/turtle1/pose` continuously streams position data regardless of whether anything is listening.
- **Services** provide synchronous, request–response communication. The `/reset` and `/spawn` services produced immediate, one-time effects on the simulation.
- **rqt** provides a convenient graphical interface for inspecting the ROS 2 graph, monitoring topics, and calling services without writing any code.
- Sending velocity commands via `ros2 topic pub` caused continuous motion because the command was published in a loop by default. Each turtle responded only to commands sent to its own `cmd_vel` topic, demonstrating proper namespace isolation in ROS 2.
- Calling `/spawn` dynamically added a new turtle at the specified coordinates, showing how services can modify the simulation state at runtime.

---

## Conclusion

This lab provided hands-on experience with the core ROS 2 communication primitives — nodes, topics, and services — using Turtlesim as a safe, visual testbed. The rqt tool proved useful for quickly inspecting and interacting with the ROS 2 ecosystem without relying solely on the command line.
