import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartphoneNode(Node):
    def __init__(self):
        super().__init__('smartphone')
        self.subscriber = self.create_subscription(msg_type=String, 
                                                   topic='robot_news',
                                                   callback=self.callback_robot_news,
                                                   qos_profile=10)
        self.get_logger().info('Smartphone has been started.')
    
    def callback_robot_news(self, msg):
        self.get_logger().info(message=msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()