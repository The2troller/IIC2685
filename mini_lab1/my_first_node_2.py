#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyFirstNode( Node ):

  def __init__( self ):
    super().__init__( 'my_first_node' )

def main():
  rclpy.init()
  node = MyFirstNode()
  rclpy.spin( node )

if __name__ == '__main__':
  main()

