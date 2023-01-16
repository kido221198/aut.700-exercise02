# aut.700-exercise02

1. Open the terminal at the extracted folder and run colcon build

2. Run . install/setup.bash

3. Run ign gazebo building_robot.sdf in terminal 1

4. Run ros2 run ros_ign_bridge parameter_bridge /cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist in terminal 2

4.1. Run ign topic -e -t cmd_vel in another terminal to check the message on /cmd_vel

4.2. Run ros2 topic echo cmd_vel in another terminal to check the message on /cmd_vel

5. Run ros2 run ros_ign_bridge parameter_bridge /keyboard/keypress@std_msgs/msg/Int32@ignition.msgs.Int32

5.1. Run ros2 topic echo keyboard/keypress to check the message on /keyboard/keypress

5.2. Run ign topic -e -t keyboard/keypress to check the message on /keyboard/keypress

6. Run ros2 launch py_server_2 py_server_2_launch.py
   or  ros2 py_server_2 py_server
