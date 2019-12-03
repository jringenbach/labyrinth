from labyrinth.element import Element



class Node:


    def __init__(self, num):
        """Node which is a cell in the labyrinth
        
        self.num (int) : unique identifier of the node
        self.connected_to (list) : list of nodes this node is connected to
        self.list_elements (list) : list of elements on this node
        self.status (int) : status of the node during the BFS algorithm. 
            0 = Unvisited, 1 = seen connected with an other node, 2 = analyzed
        self.distance_from_start_point : distance from the start point chosen during BFS algorithm
        self.pere (Node) : node from which we reached this node"""

        self.num = num
        self.connected_to = list()
        self.list_elements = list()
        self.status = 0
        self.distance_from_start_point = 0
        self.pere = None


    def about_me(self):
        print("Node num : "+str(self.num))
        print("Distance from start point : "+str(self.distance_from_start_point))
        print("Connected to node(s) : ", end="")
        for node in self.connected_to:
            print(str(node.num)+", ", end="")
        print()



    def is_equal_to(self, other_node):
        """Test if this node is equal to an other node. Return True if it is, False else.
        
        other_node (Node) : node we test"""

        if self.num == other_node.num:
            return True
        else:
            return False



    def set_connected_to(self, other_node):
        """Set the attributes self.connected_to
        
        other_node (Node) : node connected to this node"""
        self.connected_to.append(other_node)
        


    def set_list_elements(self, element):
        """Set a self.list_elements with elements given in parameters
        
        elements (Element or list) : Element or a list of elements"""

        if type(element) is Element:
            self.list_elements.append(element)
        elif type(element) is list:
            self.list_elements.extend(element)