# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from geometry_msgs.msg import Twist


class Server(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            Int32,
            'keyboard/keypress',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        key = msg.data
        self.publish(key)

    def publish(self, key):
        try:
            msg = Twist()

            if key == 167777235:
                msg.linear.x = 0.5

            elif key == 16777237:
                msg.linear.x = -0.5

            elif key == 16777234:
                msg.angular.z = 0.5

            elif key == 16777236:
                msg.angular.z = -0.5
            # msg.linear = key_map[str(key)]['linear']
            # msg.angular = key_map[str(key)]['angular']
            self.get_logger().info('Publishing...')
            self.publisher_.publish(msg)
        except KeyError:
            pass


def main(args=None):
    rclpy.init(args=args)

    server = Server()

    rclpy.spin(server)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
