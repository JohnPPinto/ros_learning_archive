from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_path
import os

def generate_launch_description():

    urdf_path = os.path.join(get_package_share_path(package_name='my_robot_description'), 
                             'urdf', 
                             'my_robot.urdf.xacro')
    
    rviz_config_path = os.path.join(get_package_share_path(package_name='my_robot_description'), 
                                    'rviz', 
                                    'my_robot_config.rviz')
    
    robot_description_param = ParameterValue(value=Command(command=['xacro ', urdf_path]), 
                                             value_type=str)

    ld = LaunchDescription()

    robot_state_publisher_node = Node(package='robot_state_publisher',
                                      executable='robot_state_publisher',
                                      parameters=[{'robot_description': robot_description_param}])
    
    joint_state_publisher_node = Node(package='joint_state_publisher_gui',
                                      executable='joint_state_publisher_gui')
    
    rviz2_node = Node(package='rviz2', 
                      executable='rviz2',
                      arguments=['-d', rviz_config_path])
    
    ld.add_action(action=robot_state_publisher_node)
    ld.add_action(action=joint_state_publisher_node)
    ld.add_action(rviz2_node)

    return ld