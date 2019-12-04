from labyrinth.element import Element



class Node:



    def __init__(self, num, labyrinth_position=None, elements=None):
        """Node which is a cell in the labyrinth
        
        self.num (int) : unique identifier of the node
        self.connected_to (list) : list of nodes this node is connected to
        self.labyrinth_position (tuple) : tuple indicating the position of the node in the labyrinth (line, column)
        self.list_elements (list) : list of elements on this node
        self.status (int) : status of the node during the BFS algorithm. 
            0 = Unvisited, 1 = seen connected with an other node, 2 = analyzed
        self.distance_from_start_point : distance from the start point chosen during BFS algorithm
        self.pere (Node) : node from which we reached this node
        self.elements (list) : list of elements on the node"""

        self.num = num
        self.connected_to = list()
        self.labyrinth_position = labyrinth_position
        self.list_elements = list()
        self.status = 0
        self.distance_from_start_point = 0
        self.pere = None
        self.elements = elements



    def about_me(self):
        print("Node num : "+str(self.num))
        print("Distance from start point : "+str(self.distance_from_start_point))
        print("Connected to node(s) : ", end="")
        for node in self.connected_to:
            print(str(node.num)+", ", end="")
        print()



    def connected_to_is_equal(self, another_node):
        """Test if the node is connected to the same nodes as the another_node. Return True if it is, False else.
        
        another_node (Node) : The other Node Object"""

        if len(self.connected_to) == len(another_node.connected_to):
            self_connected_to = sorted(self.connected_to, key = lambda x : x.num)
            another_node_connected_to = sorted(another_node.connected_to, key = lambda x : x.num)

            for i, node in enumerate(self_connected_to):
                if not node.num_is_equal_to(another_node_connected_to[i]) or \
                not node.position_is_equal_to(another_node_connected_to[i]):
                    return False

            return True


        else:
            return False



    def find_element(self, element_to_find):
        """Find an element in the list self.elements and returns it if it has been found
    
        element_to_find (Element) : Element object that we want to find in self.elements"""

        for element in self.elements:
            if element == element_to_find:
                return element
        
        return 0



    def find_element_by_parameter(self, parameter, value):
        """Find an element in the list self.elements by its parameters and returns it
        
        parameter (string) : parameter we want to test
        value (string) : value of this parameter we want to find"""

        #If the parameter is equal to one of the attribute of the Element Object
        if parameter in ["name", "symbol", "block_agent"]:
            if parameter == "name":
                for element in self.elements:
                    if element.name == value:
                        return element

            elif parameter == "symbol":
                for element in self.elements:
                    if element.symbol == value:
                        return element

            elif parameter == "block_agent":
                for element in self.elements:
                    if element.block_agent == value:
                        return element

        else:
            return 0



    def is_equal_to(self, another_node):
        """Test if the attributes of both nodes are equal"""

        if self.num == another_node.num and \
        self.labyrinth_position == another_node.labyrinth_position and \
        self.connected_to == another_node.connected_to:
            return True

        else:
            return False



    def num_is_equal_to(self, other_node):
        """Test if this node is equal to an other node. Return True if it is, False else.
        
        other_node (Node) : node we test"""

        if self.num == other_node.num:
            return True
        else:
            return False


    def position_is_equal_to(self, other_node):
        """Test if the position of this node is equal to an other node position. Return True if it is, False else.
        
        other_node (Node) : node we test"""

        if self.labyrinth_position == other_node.labyrinth_position:
            return True
        else:
            return False



    def remove_element(self, element_to_remove):
        """Remove an element from the list of elements of this node.
        
        element_to_remove (Element) : Element Object to remove from this node.elements list"""

        self.elements.remove(element_to_remove)



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