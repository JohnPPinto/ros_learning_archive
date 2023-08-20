import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool
from functools import partial

class NumberResetCounterNode(Node):
    def __init__(self):
        super().__init__(node_name='number_reset_counter')
        self.get_logger().info(message='Number reset counter client has been started.')
        
        data = bool(input('Do you want to reset the counter: '))
        self.call_reset_counter(data=data)

    def call_reset_counter(self, data):
        client = self.create_client(srv_type=SetBool,
                                    srv_name='reset_counter')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn(message='Waiting for the server')
        
        request = SetBool.Request()
        request.data = data

        future = client.call_async(request=request)
        future.add_done_callback(callback=partial(self.callback_call_reset_counter, data=data))

    def callback_call_reset_counter(self, future, data):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info(message=f'Response from the server: {response.message}')
            else:
                self.get_logger().info(message=f'Response from the server: {response.message}')
        except Exception as e:
            self.get_logger().error(message=f'Service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberResetCounterNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()