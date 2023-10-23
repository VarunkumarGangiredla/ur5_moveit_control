#!/usr/bin/env python
import sys
import rospy
import moveit_commander
from moveit_commander import MoveGroupCommander

class UR5MoveitControl:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('ur5_moveit_control', anonymous=True)
        
        self.move_group = MoveGroupCommander("manipulator")
        self.move_group.set_planning_time(5)  # Set the maximum time MoveIt! is allowed to plan

    def move_to_joint_angles(self, joint_angles):
        self.move_group.set_joint_value_target(joint_angles)
        plan = self.move_group.go(wait=True)
        return plan

if __name__ == '__main__':
    try:
        ur5_moveit_control = UR5MoveitControl()
        
        # Define the target joint angles in radians
        target_joint_angles = [0.2, -2.2, 1.0, -1.0, -1.5, 0.0]  # Example joint angles
        
        rospy.loginfo("Moving to target joint angles...")
        plan = ur5_moveit_control.move_to_joint_angles(target_joint_angles)
        
        if plan:
            rospy.loginfo("Successfully moved to the target joint angles!")
        else:
            rospy.logwarn("Failed to reach the target joint angles.")
        
    except rospy.ROSInterruptException:
        pass
