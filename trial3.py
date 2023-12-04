#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import time

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        self.publisher = self.create_publisher(Float64MultiArray, '/position_controller/commands', 10)

    def publish_command(self, data):
        command_msg = Float64MultiArray()
        command_msg.data = data
        self.publisher.publish(command_msg)
        self.get_logger().info('Published command: %s' % command_msg.data)

def main(args=None):
    rclpy.init(args=args)
    command_publisher = CommandPublisher()

    # Commands
    initial_command = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    final_command_1 = [-1.07, -1.65, 0.36, -1.44, -0.32, -0.32, 0.0]
    final_command_2 = [0.0, 0.29, 2.05, -1.68, 0.0, 0.0, 0.0]

    # First, go from initial_command to final_command_1
    velocity_1 = [(f - i) / 100 for f, i in zip(final_command_1, initial_command)]
    commands_1 = [initial_command]
    for _ in range(1, 100):
        new_command = [i + v for i, v in zip(commands_1[-1], velocity_1)]
        commands_1.append(new_command)

    commands_1.append(final_command_1)

    for command in commands_1:
        command_publisher.publish_command(command)
        time.sleep(0.1)  # Sleep for 1 second

    time.sleep(3)
    
    # Second, go from final_command_1 to final_command_2
    velocity_2 = [(f - i) / 100 for f, i in zip(final_command_2, final_command_1)]
    commands_2 = [final_command_1]
    for _ in range(1, 100):
        new_command = [i + v for i, v in zip(commands_2[-1], velocity_2)]
        commands_2.append(new_command)

    commands_2.append(final_command_2)

    for command in commands_2:
        command_publisher.publish_command(command)
        time.sleep(0.1)  # Sleep for 1 second

    command_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Float64MultiArray
# import time

# class CommandPublisher(Node):
#     def __init__(self):
#         super().__init__('command_publisher')
#         self.publisher = self.create_publisher(Float64MultiArray, '/position_controller/commands', 10)

#     def publish_command(self, data):
#         command_msg = Float64MultiArray()
#         command_msg.data = data
#         self.publisher.publish(command_msg)
#         self.get_logger().info('Published command: %s' % command_msg.data)

# def main(args=None):
#     rclpy.init(args=args)
#     command_publisher = CommandPublisher()

#     # Initial and final joint values
#     initial_command = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#     final_command = [0.0, 0.29, 2.05, -1.68, 0.0, 0.0, 0.0]

#     # Velocity calculation
#     velocity = [(f - i) / 20 for f, i in zip(final_command, initial_command)]

#     # Commands
#     commands = [initial_command]
#     for _ in range(1, 20):
#         new_command = [i + v for i, v in zip(commands[-1], velocity)]
#         commands.append(new_command)

#     for command in commands:
#         command_publisher.publish_command(command)
#         time.sleep(0.25)  # Sleep for 1 second

#     command_publisher.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Float64MultiArray

# class CommandPublisher(Node):
#     def __init__(self):
#         super().__init__('command_publisher')
#         self.publisher = self.create_publisher(Float64MultiArray, '/position_controller/commands', 10)

#     def publish_command(self, data):
#         command_msg = Float64MultiArray()
#         command_msg.data = data
#         self.publisher.publish(command_msg)
#         self.get_logger().info('Published command: %s' % command_msg.data)

# def main(args=None):
#     rclpy.init(args=args)
#     command_publisher = CommandPublisher()

#     # Commands
#     commands = [
#         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
#         [1.57, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
#         [0.0, 1.57, 0.0, 0.0, 0.0, 0.0, 0.0],
#         [0.0, 0.0, 1.57, 0.0, 0.0, 0.0, 0.0],
#         [0.0, 0.0, 0.0, 1.57, 0.0, 0.0, 0.0],
#         [0.0, 0.0, 0.0, 0.0, -1.57, 0.0, 0.0],
#         [-1.07, -1.65, 0.36, -1.44, -0.32, -0.32, 0.0],
#         [0.0, 0.29, 2.05, -1.68, 0.0, 0.0, 0.0]
#     ]

#     for command in commands:
#         command_publisher.publish_command(command)
#         rclpy.spin_once(command_publisher, timeout_sec=1.0)  # Spin for 1 second

#     command_publisher.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Float64MultiArray

# class PositionController(Node):
#     def __init__(self):
#         super().__init__('position_controller')
#         self.publisher = self.create_publisher(Float64MultiArray, '/position_controller/commands', 10)
#         self.timer = self.create_timer(1.0, self.publish_positions)
#         self.time_elapsed = 0

#     def publish_positions(self):
#         msg = Float64MultiArray()
        
#         if self.time_elapsed < 5:
#             # Publish initial positions for the first 5 seconds
#             msg.data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#         else:
#             # Publish zeros for the next 5 seconds
#             msg.data = [0.0, 0.29, 2.05, -1.68, 0.0, 0.0, 0.0]

#         self.publisher.publish(msg)
#         self.get_logger().info(f'Publishing positions: {msg.data}')

#         self.time_elapsed += 1
#         if self.time_elapsed > 10:
#             self.timer.cancel()

# def main(args=None):
#     rclpy.init(args=args)
#     position_controller = PositionController()
#     rclpy.spin(position_controller)
#     position_controller.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
