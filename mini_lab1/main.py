#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import sys

from threading import Thread
#####################################################################################################

class Client( Node ):

  def __init__( self, mytopic, othertopic):
    super().__init__( mytopic )
    self.subscription = self.create_subscription(
        String,
        othertopic,
        self.listener_callback,
        1 )
    self.publisher_obj = self.create_publisher( String, mytopic, 10 )

  def listener_callback( self, msg ):
    print( '[received] %s' % msg.data )

  def send_message( self, message):
    msg = String()
    msg.data = message
    self.publisher_obj.publish( msg )
#####################################################################################################


def main( args = None ):
  rclpy.init( args = args )

  client = Client(sys.argv[1], sys.argv[2])
  client_thread = Thread(target=rclpy.spin, args=(client,), daemon=True)
  client_thread.start()
  try:
    while True:
      msg = input()
      if msg == "":
        break
      client.send_message(msg)

  finally:
    client_thread.join()
    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
  main()