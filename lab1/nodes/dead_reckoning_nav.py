#!/usr/bin/env python3
#? ^ Le dice a bash "ejecuta esto con python3" ^
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
import time
import numpy as np
#a
class Nodo_movimiento(Node): #? Modificar nombre de clase

    def __init__(self):
        super().__init__("node_name") #? Modificar nombre del nodo
        self.publisher = self.create_publisher( Twist, "/cmd_vel", 10 )

        self.init_communications()

        self.setup_parameters()

        self.mover_robot_a_destino((0.7, 1.0, 0.0))
        
    def setup_parameters(self): #? Inicializar parámetros de ejecución
        self.velocity.linear.x = 0.0
        self.velocity.angular.z = 0.0 

    def init_communications(self): #? Crear Comunicaciones (Tópicos/Servicios)
        self.velocity = Twist()

    def aplicar_velocidad(self, speed_command_list):
        for command in speed_command_list:
            actual_time = self.get_clock().now().nanoseconds / 1e9
            self.get_logger().info( 'publishing speed (%f, %f)' % (command[0], command[1]) )
            self.velocity.linear.x = command[0]
            self.velocity.angular.z = command[1]
            while self.get_clock().now().nanoseconds / 1e9 - actual_time <= command[2]:
                self.publisher.publish(self.velocity)
                time.sleep(0.01)
        self.velocity.linear.x = 0.0
        self.velocity.angular.z = 0.0
        self.publisher.publish(self.velocity)
        
    def mover_robot_a_destino(self, goal_pose):
        speed_command_list = []
        x = goal_pose[0]
        y = goal_pose[1]
        angle = goal_pose[2]
        speed_command_list.append((0.2, 0.0, x / 0.2))
        speed_command_list.append((0.0, 1.0, np.deg2rad(90.0) + 0.15))
        speed_command_list.append((0.2, 0.0, y / 0.2))
        seconds = angle - np.deg2rad(90.0) - 0.15
        if seconds >= 0.0:
            speed_command_list.append((0.0, 1.0, seconds))
        else:
            speed_command_list.append((0.0, -1.0, abs(seconds)))
        self.aplicar_velocidad(speed_command_list)
        

def main(args=None):
    rclpy.init(args=args) #? Inicializa ROS
    node = MyNode() #? Instancia de un nodo de clase MyNode
    rclpy.spin(node) #? Permite ejecución continua de un nodo
    rclpy.shutdown() #? Cierra el nodo al terminar la ejecución
    
if __name__ == "__main__":
    main()