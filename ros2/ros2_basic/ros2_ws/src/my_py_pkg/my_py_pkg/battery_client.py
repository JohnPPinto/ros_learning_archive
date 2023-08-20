import rclpy
from rclpy.node import Node
from my_robot_interface.srv import LedControl
from functools import partial
import time


class BatteryClientNode(Node):
    def __init__(self):
        super().__init__(node_name='battery_client')
        self.get_logger().info(message='Battery client has been started.')

        battery_status = 'empty'

        
        while True:
            if battery_status == 'empty':        
                self.led_number = 3
                self.state = 'on'
                self.call_led_panel_server(led_number=self.led_number,
                                           state=self.state)
                time.sleep(6)
                self.get_logger().info(message=f'Battery status: {battery_status}')
                self.state = 'off'
                battery_status = 'full'

            elif battery_status == 'full':
                self.call_led_panel_server(led_number=self.led_number,
                                           state=self.state)
                time.sleep(4)
                self.get_logger().info(message=f'Battery status: {battery_status}')
                self.state = 'on'
                battery_status = 'empty'

    def call_led_panel_server(self, led_number, state):
        client = self.create_client(srv_type=LedControl,
                                    srv_name='set_led')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn(message='Waiting, server has not started.')
        
        request = LedControl.Request()
        request.led_number = led_number
        request.state = state

        future = client.call_async(request=request)
        future.add_done_callback(callback=partial(self.callback_call_led_panel_server, 
                                                  led_number=led_number,
                                                  state=state))

    def callback_call_led_panel_server(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info(message=f'Response received for LED no. {led_number} and state {state}: {response.success}')

        except Exception as e:
            self.get_logger().error(message=f'Service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryClientNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()