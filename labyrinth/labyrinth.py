#Python libraries
import xlrd

#Project libraries
from labyrinth.node import Node
from labyrinth.element import Element



class Labyrinth:



    def __init__(self, file_name=None):
        """
        file_name (str) : name of the file where the labyrinth is saved
        labyrinth (list) : list of every line of the labyrinth
        labyrinth_nodes (list) : list of each Node object on each line
        list_empty_nodes (list) : list of Node objects containg empty spaces
        list_wall_nodes (list) : list of Node objects containing walls
        start_point (tuple) : coordinates of the start point of the labyrinth
        exit_point (tuple) : coordinates of the exit of the labyrinth
        """

        self.file_name = file_name
        self.list_empty_nodes = list()
        self.list_wall_nodes = list()
        self.labyrinth = list()
        self.labyrinth_nodes = list()
        self.start_point = tuple()
        self.end_point = tuple()

        #If a file_name is given to get the labyrinth, we get the labyrinth and set the list of nodes
        if self.file_name is not None:
            self.labyrinth = self.get_labyrinth_from_file_name(self.file_name)
            self.set_datas_from_labyrinth()
            self.set_connection_between_nodes()




    def initialization_list_empty_nodes(self, n):
        """Initialize all the nodes in self.list_empty_nodes for the BFS algorithm
        
        n : number of nodes, so it represents the maximum distance that cannot be reached with BFS algorithm"""

        for node in self.list_empty_nodes:
            node.status = 0
            node.distance_from_start_point = n+1
            node.pere = None



    def breadth_first_search(self, start_point):
        """BFS algorithm indicating the shortest distance between start_point and each node
        
        start_point (Node object) : Node where we start the algorithm"""

        #Initial situation of the algorithm
        queue = [start_point]
        start_point.status = 1
        start_point.distance_from_start_point = 0
        
        #While the queue is not empty, we analyze the nodes in it to empty it step by step
        while(len(queue) > 0):
            node_to_analyze = queue[0]
            for node in node_to_analyze.connected_to:
                if node.status == 0:
                    node.pere = node_to_analyze
                    node.distance_from_start_point = queue[0].distance_from_start_point + 1
                    node.status = 1
                    queue.append(node)
            queue.pop(0)
            node_to_analyze.status = 2



    def equals_list_empty_nodes(self, other_list_empty_nodes):
        """Test if this labyrinth list of nodes is equal to an other list of nodes. Return True if the lists are the same, False else.
        
        other_list_empty_nodes (list) : list of Node object"""

        #If the two list of nodes have different lengths, they are automatically different
        if len(self.list_empty_nodes) != len(other_list_empty_nodes):
            return False
        else:

            #We sort both list of nodes
            list_empty_nodes = sorted(self.list_empty_nodes, key=lambda x : x.num)
            other_list_empty_nodes = sorted(other_list_empty_nodes, key=lambda x : x.num)

            #For each node in both lists
            for i, node in enumerate(list_empty_nodes):

                #We check if the length of the list of the nodes they are connected to are the same
                if len(node.connected_to) != len(other_list_empty_nodes[i].connected_to):
                    return False
                else:
                    #We check if the connection between the nodes in both list is the same
                    node_connected_to = sorted(node.connected_to, key=lambda x : x.num)
                    other_node_connected_to = sorted(list_empty_nodes[i].connected_to, key=lambda x : x.num)
                    for j, node_connec in enumerate(node_connected_to):
                        if node_connec.num != other_node_connected_to[j].num:
                            return False
            return True
                        



    def get_labyrinth_from_file_name(self, file_name):
        """Get every line of the labyrinth from a file with the name stocked in self.file_name"""

        excel_file = xlrd.open_workbook(self.file_name)
        labyrinth = list()
        for sheet in excel_file.sheets():
            for i in range(sheet.nrows):
                row = list()
                for j in range(sheet.ncols):
                    row.append(sheet.cell_value(i, j))
                labyrinth.append(row)

        return labyrinth



    def move_to_exit(self):
        """Move the Agent through the labyrinth to reach the exit point"""
        pass



    def print_list_of_nodes(self):
        """Print details of every node with information collected after BFS algorithm"""

        for node in self.list_empty_nodes:
            print("--------------------------")
            print("Node num : "+str(node.num))
            print("Node distance from start point : "+str(node.distance_from_start_point))
            if node.pere is None:
                print("Pas de père")
            else:
                print("Num du père : "+str(node.pere.num))



    def print_labyrinth(self):
        """Print the labyrinth and its element in the terminal"""

        for line in self.labyrinth_nodes:
            for column in line:
                #If there is only one element, we print its symbol
                if len(column.elements) == 1:
                    print(column.elements[0].symbol, end="")

                #Else, we are looking for the Agent element, and we print its symbol
                else:
                    for element in column.elements:
                        if element.name == "Agent":
                            print(element.symbol, end="")
            print()
                       
                    



    def set_connection_between_nodes(self):
        """Set every attributes connected_to for every node in self.list_empty_nodes. It establishes the connection between nodes."""

        for i, node in enumerate(self.list_empty_nodes):
            line = node.labyrinth_position[0]
            column = node.labyrinth_position[1]

            for j in range(i+1, len(self.list_empty_nodes)):
                line_j = self.list_empty_nodes[j].labyrinth_position[0]
                column_j = self.list_empty_nodes[j].labyrinth_position[1]
                
                if i != j and ((line == line_j and column == column_j - 1) \
                or (line == line_j and column == column_j + 1) \
                or (column == column_j and line == line_j - 1) \
                or (column == column_j and line == line_j + 1)) \
                and (not node in self.list_empty_nodes[j].connected_to) \
                and (not self.list_empty_nodes[j] in node.connected_to):
                    node.connected_to.append(self.list_empty_nodes[j])
                    self.list_empty_nodes[j].connected_to.append(node)



    def set_datas_from_labyrinth(self):
        """Create the list of nodes depending on the labyrinth read in a xls file and set self.start_point and self.exit_point"""

        node_number = 1

        for i, line in enumerate(self.labyrinth):
            row = list()
            for j, column in enumerate(line):
                node = Node(node_number, (i,j))

                #If it is an empty space
                if column == "":
                    element = Element("Empty", " ", False)
                    node.elements = [element]
                    self.list_empty_nodes.append(node)

                #If this is the start point
                elif column == "S":
                    element = Element("Start", "S", False)
                    agent = Element("Agent", "A", False)
                    node.elements = [element, agent]
                    self.start_point = node

                #If this is the exit
                elif column == "E":
                    element = Element("Exit", "E", False)
                    node.elements = [element]
                    self.exit_point = node

                #If this is a wall
                elif column == "X":
                    element = Element("Wall", "X", True)
                    node.elements = [element]
                    self.list_wall_nodes.append(node)

                row.append(node)
                node_number += 1
            self.labyrinth_nodes.append(row)





