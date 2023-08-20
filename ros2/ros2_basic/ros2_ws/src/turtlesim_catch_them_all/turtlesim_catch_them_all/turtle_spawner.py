import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from my_robot_interface.msg import Turtle
from my_robot_interface.msg import TurtleArray
from my_robot_interface.srv import CatchTurtle

from functools import partial
import random
import math

class TurtleSpawnerNode(Node):
    def __init__(self):
        super().__init__(node_name='turtle_spawner')
        self.get_logger().info(message='Turtle spawner node has been started...')

        # Declaring Ros2 parameters
        self.declare_parameters(namespace='params', 
                                parameters=[('name_prefix', 'turtle_'), 
                                            ('counter', 0),
                                            ('spawn_frequency', 1.0)])
        self.name_prefix = self.get_parameter(name='params.name_prefix').value
        self.counter = self.get_parameter(name='params.counter').value
        self.spawn_frequency = self.get_parameter(name='params.spawn_frequency').value
        
        # A timer for spawing a new turtle at a  constant rate
        self.create_timer(timer_period_sec= self.spawn_frequency, 
                          callback=self.callback_spawn_interval)

        # A list for collecting the spawned turtle's name and coordinates
        self.alive_turtle_array = []

        # Creating a topic and publishing the spawn details
        self.alive_turtles_publisher = self.create_publisher(msg_type=TurtleArray,
                                                             topic='alive_turtles',
                                                             qos_profile=10)
        
        # Creating a service for when the turtle has caught the target
        self.catch_turtle_service = self.create_service(srv_type=CatchTurtle, 
                                                        srv_name='catch_turtle', 
                                                        callback=self.callback_catch_turtle_service)

    # **************** Turtlesim Spawn - client *************** #

    # A spawn interval callback for initiating the client request at certain frequency
    def callback_spawn_interval(self):
        x = round(random.uniform(a=0.00, b=11.00), 2)
        y = round(random.uniform(a=0.00, b=11.00), 2)
        theta = round(random.uniform(a=0.00, b=2*math.pi), 2)
        self.counter += 1
        name = self.name_prefix + str(self.counter)
        self.call_turtlesim_spawn_service(x=x, y=y, theta=theta, name=name)

    # Creating a client request to the spawn service
    def call_turtlesim_spawn_service(self, x, y, theta, name):
        turtle_spawn_client = self.create_client(srv_type=Spawn,
                                                 srv_name='spawn')
        while not turtle_spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(message='Waiting for the server...')

        # Sending the request
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = name

        # Getting the future object
        future = turtle_spawn_client.call_async(request=request)
        future.add_done_callback(callback=partial(self.callback_call_turtlesim_spawn, x=x, y=y, theta=theta))

    # Creating a callback for getting the response from future object
    def callback_call_turtlesim_spawn(self, future, x, y, theta):
        try:
            response = future.result()
            if response.name != '':
                self.get_logger().info(message=f'Response received on sending request {x}, {y}: {response.name}')
                
                # Providing the message to the publisher
                new_spawned_turtle = Turtle()
                new_spawned_turtle.x = x
                new_spawned_turtle.y = y
                new_spawned_turtle.theta = theta
                new_spawned_turtle.name = response.name
                self.alive_turtle_array.append(new_spawned_turtle)
                self.publish_alive_turtles()

        except Exception as e:
            self.get_logger().error(message='Service call failed: {e}')
    
    # **************** /Turtlesim Spawn - client *************** #

    # **************** Alive Turtles - Publisher ***************** #

    def publish_alive_turtles(self):
        msg = TurtleArray()
        msg.turtles = self.alive_turtle_array
        self.alive_turtles_publisher.publish(msg=msg)
        
    # **************** /Alive Turtles - Publisher ***************** #

    # **************** Catch Turtle - Service ****************#
    
    def callback_catch_turtle_service(self, request, response):
        self.call_turtlesim_kill_service(name=request.name)
        response.success = True
        return response

    # Killing the target turtle when caught, requesting the server to kill
    def call_turtlesim_kill_service(self, name):
        turtle_kill_client = self.create_client(srv_type=Kill,
                                                 srv_name='kill')
        while not turtle_kill_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(message='Waiting for the server...')

        # Sending the request
        request = Kill.Request()
        request.name = name

        # Getting the future object
        future = turtle_kill_client.call_async(request=request)
        future.add_done_callback(callback=partial(self.callback_call_turtlesim_kill, name=name))

    # Creating a callback for getting the response from future object
    def callback_call_turtlesim_kill(self, future, name):
        try:
            future.result()
            for i, turtle in enumerate(self.alive_turtle_array):
                if turtle.name == name:
                    del self.alive_turtle_array[i]
                    self.publish_alive_turtles()
                    break
            
        except Exception as e:
            self.get_logger().error(message='Service call failed: {e}')
    
    # **************** /Catch Turtle - Service ****************#

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()