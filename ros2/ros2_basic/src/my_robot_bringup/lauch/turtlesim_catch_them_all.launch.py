from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    turtlesim_node = Node(package='turtlesim',
                          executable='turtlesim_node')
    turtlesim_spawner_node = Node(package='turtlesim_catch_them_all',
                                  executable='turtle_spawner',
                                  parameters=[{'name_prefix': 'my_turtle_'},
                                              {'counter': 100},
                                              {'spawn_frequency': 1.0}])
    turtlesim_controller_node = Node(package='turtlesim_catch_them_all',
                                     executable='turtle_controller',
                                     parameters=[{'catch_closest_turtle_first': True}])
    
    ld.add_action(action=turtlesim_node)
    ld.add_action(action=turtlesim_spawner_node)
    ld.add_action(action=turtlesim_controller_node)
    
    return ld