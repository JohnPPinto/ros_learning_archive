import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__(node_name='number_publisher')
        # Single parameter declared
        # self.declare_parameter(name='number_to_publish', value=2)
        # self.declare_parameter(name='publish_frequency', value=1.0)

        # multi parameter declared    
        self.declare_parameters(namespace='params',
                                parameters=[('number_to_publish', 2), 
                                            ('publish_frequency', 1.0)])

        self.number = self.get_parameter(name='params.number_to_publish').value
        self.frequency = self.get_parameter(name='params.publish_frequency').value

        self.publisher = self.create_publisher(msg_type=Int64,
                                               topic='number',
                                               qos_profile=10)
        self.timer = self.create_timer(timer_period_sec=(1.0 / self.frequency), 
                                       callback=self.publish_number)
        self.get_logger().info(message='Number publisher node has been started.')
    
    def publish_number(self):
        msg = Int64()
        msg.data = self.number
        self.publisher.publish(msg=msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()