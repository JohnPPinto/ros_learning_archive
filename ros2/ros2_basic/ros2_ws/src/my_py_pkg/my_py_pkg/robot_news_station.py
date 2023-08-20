#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__(node_name='robot_news_station')
        self.declare_parameter(name='robot_name', value='Robot123')
        self.robot_name = self.get_parameter(name='robot_name').value
        self.publisher = self.create_publisher(msg_type=String,
                                               topic='robot_news',
                                               qos_profile=10)
        self.timer = self.create_timer(timer_period_sec=0.5, callback=self.publish_news)
        self.get_logger().info(message='Robot news station has been started.')
        
    def publish_news(self):
        msg = String()
        msg.data = f'Hello, this {self.robot_name} from robot news station.'
        self.publisher.publish(msg=msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()