import rclpy
from rclpy.node import Node
from my_robot_interface.msg import LedStatus
from my_robot_interface.srv import LedControl

class LedPanelServerNode(Node):
    def __init__(self):
        super().__init__(node_name='led_panel_server')
        self.declare_parameter(name='led_panel_state', value=[0, 0, 0])

        self.led_current_status = self.get_parameter(name='led_panel_state').value

        self.server = self.create_service(srv_type=LedControl,
                                          srv_name='set_led',
                                          callback=self.callback_set_led)
        
        if all(i >= 0 and i <=1 for i in self.led_current_status):
            self.publisher = self.create_publisher(msg_type=LedStatus,
                                               topic='led_states',
                                               qos_profile=10)
        else:
            self.get_logger().error(message='Wrong value was provided, LED State can be only True or False (0 or 1).')
        
        self.timer = self.create_timer(timer_period_sec=1.0, 
                                       callback=self.callback_publish_led_state)
        
        self.get_logger().info(message='Led Panel Server has been started...')

    def callback_set_led(self, request, response):
        if (request.state == 'on' and (request.led_number >= 1 and request.led_number <= 3)):
            self.led_current_status[request.led_number - 1] = 1
            if self.led_current_status[request.led_number - 1] == 1:
                response.success = True
            else:
                response.success = False
            self.get_logger().info(message=f'LED State is been updated: LED number: {request.led_number} and State: {request.state}')

        elif (request.state == 'off' and (request.led_number >= 1 and request.led_number <= 3)):
            self.led_current_status[request.led_number - 1] = 0
            if self.led_current_status[request.led_number - 1] == 0:
                response.success = True
            else:
                response.success = False
            self.get_logger().info(message=f'LED State is been updated: LED number: {request.led_number} and State: {request.state}')

        else:
            self.get_logger().warn(message=f'Wrong request provided: LED number: {request.led_number} and State: {request.state}')
        
        return response
    
    def callback_publish_led_state(self):
        msg = LedStatus()
        msg.led_panel_state = self.led_current_status
        self.publisher.publish(msg=msg)

def main(args=None):
    rclpy.init(args=args)
    node = LedPanelServerNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()