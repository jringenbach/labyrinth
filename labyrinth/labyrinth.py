from labyrinth.node import node



class Labyrinth:



    def __init__(self):
        self.list_nodes = list()



    def initialization_list_nodes(self, n):
        """Initialize all the nodes in self.list_nodes for the BFS algorithm
        
        n : number of nodes, so it represents the maximum distance that cannot be reached with BFS algorithm"""

        for node in self.list_nodes:
            node.status = 0
            node.distance_from_start_point = n+1
            node.pere = None



    def print_list_of_nodes(self):
        """Print details of every node with information collected after BFS algorithm"""
        
        for node in self.list_nodes:
            print("--------------------------")
            print("Node num : "+str(node.num))
            print("Node distance from start point : "+str(node.distance_from_start_point))
            if node.pere is None:
                print("Pas de père")
            else:
                print("Num du père : "+str(node.pere.num))
