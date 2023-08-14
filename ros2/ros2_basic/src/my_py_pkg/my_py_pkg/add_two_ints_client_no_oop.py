import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    
    node = Node(node_name='add_two_ints_no_opp')
    
    client = node.create_client(srv_type=AddTwoInts,
                                srv_name='add_two_ints')
    
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().warn(message='Waiting for the Server Add Two Ints')
    
    request = AddTwoInts.Request()
    request.a = int(input('Enter a number: '))
    request.b = int(input('Enter another number: '))

    future = client.call_async(request=request)

    rclpy.spin_until_future_complete(node=node, future=future)

    try:
        response = future.result()
        node.get_logger().info(message=f'{request.a} + {request.b} = {response.sum}')
    except Exception as e:
        node.get_logger().error(message=f'Service call failed: {e}')

    rclpy.shutdown()

if __name__ == '__main__':
    main()