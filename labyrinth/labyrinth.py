from labyrinth.node import Node



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
