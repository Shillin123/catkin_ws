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
  env = {'IGN_GAZEBO_SYSTEM_PLUGIN_PATH':
           ':'.join([environ.get('IGN_GAZEBO_SYSTEM_PLUGIN_PATH', default=''),
                     environ.get('LD_LIBRARY_PATH', default='')])}
  pkg_ros_ign_gazebo = get_package_share_directory('ros_ign_gazebo')
  ign_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_ign_gazebo, 'launch', 'ign_gazebo.launch.py')),
        launch_arguments={
            'ign_args': '-r ~/catkin_ws/src/diff_car/diff_car.sdf'
        }.items(),
    )

  bridge = Node(
        package='ros_ign_bridge',
        executable='parameter_bridge',
        arguments=['/diff_drive_base_controller/cmd_vel_unstamped@geometry_msgs/msg/Twist@ignition.msgs.Twist'],
        output='screen'
  )
  return LaunchDescription([
        ign_gazebo,
        bridge
  ])

