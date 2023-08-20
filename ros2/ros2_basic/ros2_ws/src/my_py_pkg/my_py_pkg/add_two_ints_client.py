import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__(node_name='add_two_ints_client')
        a = int(input('Enter a number: '))
        b = int(input('Enter another number: '))
        self.call_add_two_ints_server(a=a, b=b)

    def call_add_two_ints_server(self, a, b):
        client = self.create_client(srv_type=AddTwoInts, srv_name='add_two_ints')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn(message='Waiting for the server.')
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request=request)
        future.add_done_callback(partial(self.callback_call_add_two_ints, a=a, b=b))

    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(message=f'{a} + {b} = {response.sum}')
        except Exception as e:
            self.get_logger().error(message=f'Service call failed: {e}')

def main(args=None):
    rclpy.init()
    node = AddTwoIntsClientNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()