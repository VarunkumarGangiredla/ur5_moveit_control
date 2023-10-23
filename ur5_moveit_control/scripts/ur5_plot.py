import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
import math

def joint_states_callback(msg):
    # Get the current joint positions
    joint_positions = msg.position

    # Calculate sine wave joint angles
    sine_angles = [math.sin(pos) for pos in joint_positions]

    # Publish the sine wave joint angles
    sin_angles_msg = JointState()
    sin_angles_msg.position = sine_angles
    sin_angles_msg.name = msg.name

    pub.publish(sin_angles_msg)

def main():
    rospy.init_node('joint_sinangles_publisher')

    # Subscribe to the /joint_states topic
    rospy.Subscriber('/joint_states', JointState, joint_states_callback)

    # Publish to the /joint_sinangles topic
    global pub
    pub = rospy.Publisher('/joint_sinangles', JointState, queue_size=10)

    # Keep the node running
    rospy.spin()

if __name__ == '__main__':
    main()
