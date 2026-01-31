from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=[
                "--x", "-0.262",
                "--y", "-0.250",
                "--z", "-0.522",
                "--roll", "0",
                "--pitch", "0",
                "--yaw", "0",
                "--frame-id", "body",
                "--child-frame-id", "base_link",
            ],
            output="screen",
        )
    ])
