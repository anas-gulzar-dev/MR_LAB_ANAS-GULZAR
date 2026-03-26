1): Brief Description

This lab introduced the basics of ROS 2 development, including Linux terminal usage, workspace setup, and Python package creation. I created a ROS 2 workspace, built a Python package named my_first_pkg, and implemented a simple node that prints a welcome message, maintains a run counter, and demonstrates ROS parameter usage.

2): Commands Used

Workspace and package setup:
     mkdir -p ~/ros2_ws_anas/src
     cd ~/ros2_ws_anas/src
     ros2 pkg create --build-type ament_python my_first_pkg

Building and sourcing:
     cd ~/ros2_ws_anas
     colcon build
     source setup.bash
Running the node:
     ros2 run my_first_pkg simple_node
     ros2 run my_first_pkg simple_node --ros-args -p student_name:=Anas

3): Problems Faced and Solutions

Parameter warning: Received a deprecation warning when declaring the student_name parameter. The node still worked, but I learned to provide a default value or type for future compatibility.
Run counter file location: Ensured the counter file was stored in the correct directory using os.path.dirname(__file__).
Forgetting to rebuild/source: Sometimes changes didn’t appear until I rebuilt with colcon build and sourced the workspace again.
4): Reflection

This lab helped me understand the ROS 2 development workflow, from workspace setup to package and node creation. I practiced using the Linux terminal and learned the importance of proper file permissions and workspace sourcing. Implementing the run counter and parameter logic gave me hands-on experience with file I/O and ROS 2 parameters. Troubleshooting build and execution issues improved my debugging skills. I now feel more confident in creating and managing ROS 2 packages and nodes. The step-by-step instructions and immediate feedback from the terminal made the learning process clear and effective. I look forward to building more complex nodes and exploring ROS 2 communication concepts in future labs.



