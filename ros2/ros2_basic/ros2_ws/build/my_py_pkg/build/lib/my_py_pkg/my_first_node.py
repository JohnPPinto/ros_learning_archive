#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('py_test')
        self.get_logger().info('Hello ROS2')
        self.counter = 0
        self.create_timer(timer_period_sec=0.5, callback=self.timer_callback)

    def timer_callback(self):
        self.counter += 1
        self.get_logger().info('Hello World!' + str(self.counter))


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()