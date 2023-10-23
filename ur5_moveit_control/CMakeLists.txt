cmake_minimum_required(VERSION 2.8.3)
project(ur5_moveit_control)

find_package(catkin REQUIRED COMPONENTS
  rospy
  moveit_commander
  moveit_msgs
  std_msgs
  geometry_msgs
  sensor_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/ur5_ctrl.py
  scripts/ur5_plot.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
