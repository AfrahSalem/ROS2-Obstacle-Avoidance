import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WallAvoider(Node):
    def __init__(self):
        super().__init__('wall_avoider')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.listener_callback, 10)
        self.move = Twist()

    def listener_callback(self, msg):
        # On vérifie la distance devant (index 0)
        # On utilise 'min' pour éviter les erreurs si une valeur est invalide
        front_distance = msg.ranges[0]
        
        self.get_logger().info(f'Distance : {front_distance:.2f}m')

        if front_distance < 0.7: 
            self.move.linear.x = 0.0      # Stop
            self.move.angular.z = 0.5     # Tourne à gauche
            self.get_logger().info('OBSTACLE ! Je tourne...')
        else:
            self.move.linear.x = 0.2      # Avance
            self.move.angular.z = 0.0     # Tout droit
            self.get_logger().info('Route libre.')
        
        self.publisher_.publish(self.move)

def main(args=None):
    rclpy.init(args=args)
    node = WallAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
