import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__(node_name='number_counter')
        self.counter = 0
        self.subscriber = self.create_subscription(msg_type=Int64,
                                                   topic='number',
                                                   callback=self.callback_number_publisher,
                                                   qos_profile=10)
        self.publisher = self.create_publisher(msg_type=Int64,
                                               topic='number_count',
                                               qos_profile=10)
        self.service = self.create_service(srv_type=SetBool,
                                           srv_name='reset_counter',
                                           callback=self.callback_reset_counter)
        self.get_logger().info(message='Number Counter has been started.')
    
    def callback_number_publisher(self, msg):
        self.counter += msg.data
        counter_msg = Int64()
        counter_msg.data = self.counter
        self.publisher.publish(msg=counter_msg)

    def callback_reset_counter(self, request, response):
        if request.data:
            self.counter = 0
            response.success = True
            response.message = 'Counter is reset to 0'
        else:
            response.success = False
            response.message = f'Counter is not reset, current status {self.counter}'
        self.get_logger().info(message=f'Service "reset_counter" data: {request.data} and counter status: {self.counter}')
        return response    

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()