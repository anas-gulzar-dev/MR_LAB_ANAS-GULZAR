1. Define: node, topic, package, workspace. Provide one sentence each.  

Node: A node is a single running program or process that performs a specific task within your robot's system.
Topic: A topic is a named communication channel where nodes can continuously send and receive streams of data.
Package: A package is a folder that bundles together your ROS 2 code, settings, and build instructions so it can be easily run and shared.
Workspace: A workspace is the main directory on your computer where you create, store, and build all of your different ROS 2 packages.

2. Explain why sourcing is required. What happens if you do not source a workspace?  

Sourcing acts as a map for your computer's terminal, telling it exactly where to find the ROS 2 tools and the specific packages you just built. If you do not source your workspace, the terminal will be blind to your code, and you will get errors like command not found or Package not found when you try to run anything.

3. What is the purpose of `colcon build`? What folders does it generate?  

The colcon build command takes your raw, human-written source code and compiles it into ready-to-run executable files that ROS 2 can understand. When it finishes, it creates three new folders alongside your src folder: build/ (for temporary files), install/ (where the final usable files are placed), and log/ (which keeps a record of the build process).

4. In your own words, explain what the `entry_points` console script does in `setup.py`.  

The entry_points script basically works like a directory lookup, linking a simple command name (like simple_node) to the exact Python function it needs to trigger. Without this link, ROS 2 wouldn't know which file or specific block of code to execute when you type the ros2 run command.

5. Draw (by hand or ASCII) a diagram showing one publisher and one subscriber connected by a topic. 

+-----------------------+                             +-----------------------+
|       Node A          |                             |        Node B         |
|     (Publisher)       |                             |     (Subscriber)      |
|                       |        /topic_name          |                       |
|  sends data out       |---------------------------->|  listens and receives |
|                       |                             |  the data             |
+-----------------------+                             +-----------------------+
