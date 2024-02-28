import os
from ament_index_python.packages import get_package_share_directory , get_search_paths
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch import LaunchDescription, Action
import launch


def generate_launch_description():  
    # Subject Information
    Subject_Number = "P1"
  
    ###### Physiological Sensor
    ros2_foxy_vernier_respiration_belt_node = Node(
            package='vernier_respiration_belt', 
            #namespace='Subject_Number',
            executable='vernier_respiration_belt_node',
            name='vernier_respiration_belt_node',
            #output='screen',
            parameters=[{'Sensor_Enable': True, 
            'Chunk_Enable': True,
            'Chunk_Length': 20,
            ### For sensor devices
            'Device_Name': 'GDX-RB 0K5016Q9',
            'Device_Sampling_Rate': 10 #unit = milliseconds
            }] 
        )
  
    return LaunchDescription([
        ros2_foxy_vernier_respiration_belt_node,        
    ])
