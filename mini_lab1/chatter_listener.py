#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import time


class MinimalSubscriber( Node ):

  def __init__( self ):
    super().__init__( 'listener' )
    self.subscription = self.create_subscription(
        String,
        'topic',
        self.listener_callback,
        1 )

  def listener_callback( self, msg ):
    self.get_logger().info( 'I heard: "%s"' % msg.data )

    # Que pasa si la callback tarda mas de lo esperado ?
    # Descomente siguiente linea y repita la prueba:
    #time.sleep( 1.0 )


def main( args = None ):
  rclpy.init( args = args )

  minimal_subscriber = MinimalSubscriber()

  rclpy.spin( minimal_subscriber )

  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  minimal_subscriber.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()

