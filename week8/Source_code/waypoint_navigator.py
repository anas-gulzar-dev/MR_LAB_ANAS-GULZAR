import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped
import time

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self._client = ActionClient(self, FollowWaypoints, 'follow_waypoints')
        # Track the current waypoint index to print updates
        self.current_wp_index = 0
        self.total_waypoints = 0

    def feedback_callback(self, feedback_msg):
        # This function is called continuously while the robot is navigating
        current_wp = feedback_msg.feedback.current_waypoint
        
        # If the waypoint index increases, it means the previous one was reached
        if current_wp > self.current_wp_index:
            self.get_logger().info(f'Reached goal {self.current_wp_index + 1}!')
            self.get_logger().info(f'Moving towards goal {current_wp + 1}...')
            self.current_wp_index = current_wp

    def send_waypoints(self, waypoints):
        self.total_waypoints = len(waypoints)
        self.current_wp_index = 0
        
        self.get_logger().info('Waiting for FollowWaypoints action server...')
        self._client.wait_for_server()
        
        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints
        self.get_logger().info(f'Sending {self.total_waypoints} waypoints...')
        
        # Attach the feedback callback when sending the goal
        send_goal_future = self._client.send_goal_async(
            goal_msg, 
            feedback_callback=self.feedback_callback
        )
        rclpy.spin_until_future_complete(self, send_goal_future)
        
        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected by server!')
            return
            
        self.get_logger().info('Goal accepted. Navigating...')
        self.get_logger().info('Moving towards goal 1...')
        
        # Wait for the entire mission to finish
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        
        # Print final success messages
        self.get_logger().info(f'Reached goal {self.total_waypoints}!')
        self.get_logger().info('All waypoints reached!')

def make_pose(x, y, yaw_w):
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = 0.0
    pose.pose.orientation.z = yaw_w
    pose.pose.orientation.w = 1.0
    return pose

def main(args=None):
    rclpy.init(args=args)
    navigator = WaypointNavigator()
    
    # Your custom waypoints
    waypoints = [
        make_pose(3.7872959281025635, 1.2330572419018555, -0.6137583757627343),   # Waypoint 1
        make_pose(1.722630485537056, -1.427899845628565, 0.9993212961514923),   # Waypoint 2
        make_pose(1.9659733827711645, 2.495532146604072, -0.052693980243234836),  # Waypoint 3
        make_pose(-0.12197858722879883, 0.37399042206395783, -0.3383568990410002),   # Waypoint 4
        make_pose(2.4797274503748863, -0.07985729475568362, -0.6125611378328013)    # Waypoint 5 (return to origin)
    ]
    
    navigator.send_waypoints(waypoints)
    navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
