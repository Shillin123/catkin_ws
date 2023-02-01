import os
from os import environ
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
def generate_launch_description():
  pkg_diff_car = get_package_share_directory('diff_car')
  diff_car = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_diff_car, 'launch', 'diff_car.launch.py'))
    )

  config = os.path.join(
        get_package_share_directory('Huang_Diffrobot'),
        'config',
        'vel.yaml'
  )

  vel = Node(
        package='Huang_Diffrobot',
        name='huang_diffrobot',
        executable='Huang_Diffrobot',
        output='screen',
        parameters=[config]
  )
  return LaunchDescription([
        diff_car,
        vel
  ])

