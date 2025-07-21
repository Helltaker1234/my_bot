# 이 사람도 rplidar a1 을 씀.
# 시리얼 포트 정도만 맞게 수정하면 될듯.

import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/serial/by-path/pci-0000:00:14.0-usb-0:7:1.0-port0',
                # 이부분을 내 우분투에 맞게 수정해야함.
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )
    ])
