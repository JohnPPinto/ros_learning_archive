import math
from functools import partial

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from my_robot_interface.msg import TurtleArray
from my_robot_interface.srv import CatchTurtle

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__(node_name='turtle_controller')
        self.get_logger().info(message='Turtle Controller node has been started...')

        # Subscribing to turtle1/pose topic
        self.pose = None
        self.turtle_pose_subscriber = self.create_subscription(msg_type=Pose,
                                                               topic='turtle1/pose',
                                                               callback=self.callback_turtle_pos,
                                                               qos_profile=10)
        
        # Creating a publisher to provide velocity details
        self.cmd_vel_publisher = self.create_publisher(msg_type=Twist,
                                                       topic='turtle1/cmd_vel',
                                                       qos_profile=10)
        self.control_loop_timer = self.create_timer(timer_period_sec=0.01, 
                                                    callback=self.callback_control_loop)
        
        # Creating a subcriber to the turtles array topic and getting the location of the spawned turtle
        self.turtles_to_catch = None
        self.alive_turtle_subscriber = self.create_subscription(msg_type=TurtleArray,
                                                                topic='alive_turtles',
                                                                callback=self.callback_alive_turtles,
                                                                qos_profile=10)
        
        # Whether to catch the closest turtle
        self.declare_parameter(name='catch_closest_turtle_first', value=False) # Declaring ros2 parameters
        self.catch_closest_turtle_first = self.get_parameter(name='catch_closest_turtle_first').value
    
    # Getting the information of Turtle1 Position
    def callback_turtle_pos(self, msg):
        self.pose = msg

    # Creating the callback for getting alive spawned turtles array
    def callback_alive_turtles(self, msg):
        if len(msg.turtles) > 0:

            # Selecting the closest turtle first as a target
            if self.catch_closest_turtle_first:
                closest_turtle = None
                closest_turtle_distance = None

                for turtle in msg.turtles:
                    dist_x = turtle.x - self.pose.x
                    dist_y = turtle.y - self.pose.y
                    distance = math.sqrt(dist_x ** 2 + dist_y ** 2)
                    if closest_turtle == None or distance < closest_turtle_distance:
                        closest_turtle = turtle
                        closest_turtle_distance = distance
                self.turtles_to_catch = closest_turtle

            else:
                self.turtles_to_catch = msg.turtles[0]

    # ************************* Publishing Turtle1 - cmd_vel *************************** #

    # Calculating the distance and angle between the turtle and the target and publishing it back
    def callback_control_loop(self):
        msg = Twist()

        if self.pose == None or self.turtles_to_catch == None:
            return
        
        # Calculate the distance to the target
        dist_x = self.turtles_to_catch.x - self.pose.x
        dist_y = self.turtles_to_catch.y - self.pose.y
        distance = math.sqrt(dist_x ** 2 + dist_y ** 2)

        if distance > 0.5:
            # linear velocity
            msg.linear.x = 2 * distance

            # angular velocity
            target_theta = math.atan2(dist_y, dist_x)
            theta_diff = target_theta - self.pose.theta

            # Normalizing the angles
            if theta_diff > math.pi:
                theta_diff -= 2 * math.pi
            elif theta_diff < -math.pi:
                theta_diff += 2 * math.pi
            
            msg.angular.z = 8 * theta_diff
        else:
            # Turtle has been caught
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            
            # Calling the catch turtle service
            self.call_catch_turtle_server(name=self.turtles_to_catch.name)
            self.turtles_to_catch = None

        # Publishing the linear and angular velocity to the topic
        self.cmd_vel_publisher.publish(msg=msg)

    # ************************* /Publishing Turtle1 - cmd_vel *************************** #

    # ************************* Catch turtle client - CatchTurtle ******************************* #

    # Creating a client request to the turtle_to_catch servies when the turtle has caught the target
    def call_catch_turtle_server(self, name):
        catch_turtle_client = self.create_client(srv_type=CatchTurtle,
                                                 srv_name='catch_turtle')
        while not catch_turtle_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(message='Waiting for the server...')

        # Sending the request
        request = CatchTurtle.Request()
        request.name = name

        # Getting the future object
        future = catch_turtle_client.call_async(request=request)
        future.add_done_callback(callback=partial(self.callback_catch_turtle, name=name))

    # Creating a callback for getting the response from future object
    def callback_catch_turtle(self, future, name):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info(message=f'Turtle {name} has been caught and killed.')
            else:
                self.get_logger().info(message=f'Turtle {name} could not be caught.')

        except Exception as e:
            self.get_logger().error(message='Service call failed: {e}')
    
    # *********************** /Catch turtle client - CatchTurtle ***************************** #


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()