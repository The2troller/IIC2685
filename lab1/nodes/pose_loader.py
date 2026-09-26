#!/usr/bin/env python3
#? ^ Le dice a bash "ejecuta esto con python3" ^
import rclpy
from rclpy.node import Node
class MyNode(Node): #? Modificar nombre de clase

    def __init__(self):
        super().__init__("node_name") #? Modificar nombre del nodo
        #? --- Atributos ---

    def setup_parameters(self): #? Inicializar parámetros de ejecución
        pass

    def init_communications(self): #? Crear Comunicaciones (Tópicos/Servicios)
        pass

    def example_cb(self): #? Callback de un tópico
        pass


def main(args=None):
    rclpy.init(args=args) #? Inicializa ROS
    node = MyNode() #? Instancia de un nodo de clase MyNode
    rclpy.spin(node) #? Permite ejecución continua de un nodo
    rclpy.shutdown() #? Cierra el nodo al terminar la ejecución
    
if __name__ == "__main__":
    main()