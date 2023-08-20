import rclpy
from rclpy.node import Node
from my_robot_interface.msg import HardwareStatus

class HardwareStatusPublisherNode(Node):
    def __init__(self):
        super().__init__(node_name='hardware_status_publisher')
        self.hw_status_publisher = self.create_publisher(msg_type=HardwareStatus,
                                                         topic='hardware_status',
                                                         qos_profile=10)
        self.timer = self.create_timer(timer_period_sec=0.5, callback=self.publish_hardware_status)
        self.get_logger().info(message='Hardware Status Publisher has been started.')

    def publish_hardware_status(self):
        msg = HardwareStatus()
        msg.temperature = 45
        msg.are_motors_ready = True
        msg.debug_message = 'Nothing special here.'
        self.hw_status_publisher.publish(msg=msg)


def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisherNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()