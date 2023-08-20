from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    robot1_node = Node(package='my_py_pkg',
                       executable='robot_news_station',
                       name='robot_news_station_giskard',
                       parameters=[{'robot_name': 'Giskard'}])
    robot2_node = Node(package='my_py_pkg',
                       executable='robot_news_station',
                       name='robot_news_station_bb8',
                       parameters=[{'robot_name': 'BB8'}])
    robot3_node = Node(package='my_py_pkg',
                       executable='robot_news_station',
                       name='robot_news_station_daneel',
                       parameters=[{'robot_name': 'Daneel'}])
    robot4_node = Node(package='my_py_pkg',
                       executable='robot_news_station',
                       name='robot_news_station_jander',
                       parameters=[{'robot_name': 'Jander'}])
    robot5_node = Node(package='my_py_pkg',
                       executable='robot_news_station',
                       name='robot_news_station_c3po',
                       parameters=[{'robot_name': 'C3PO'}])
    
    smartphone_node = Node(package='my_py_pkg',
                           executable='smartphone')
    
    ld.add_action(action=robot1_node)
    ld.add_action(action=robot2_node)
    ld.add_action(action=robot3_node)
    ld.add_action(action=robot4_node)
    ld.add_action(action=robot5_node)
    ld.add_action(action=smartphone_node)

    return ld