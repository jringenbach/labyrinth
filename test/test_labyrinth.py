from labyrinth.labyrinth import Labyrinth
from labyrinth.node import Node

def test_breadth_first_search():
    """Test labyrinth.breadth_first_search(start_point) algorithm"""

    labyrinth = Labyrinth()

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    number_of_nodes = 4

    list_nodes = [node_1, node_2, node_3, node_4]
    labyrinth.list_nodes = list_nodes
    labyrinth.initialization_list_nodes(number_of_nodes)

    #We represent the graph |1| - |2| - |3| - |4|
    node_1.set_connected_to(node_2)
    node_2.set_connected_to(node_1)
    node_2.set_connected_to(node_3)
    node_3.set_connected_to(node_2)
    node_3.set_connected_to(node_4)
    node_4.set_connected_to(node_3)

    #We set the start_point at node number 2
    labyrinth.breadth_first_search(start_point=node_2)
    assert node_1.distance_from_start_point == 1
    assert node_2.distance_from_start_point == 0
    assert node_3.distance_from_start_point == 1
    assert node_4.distance_from_start_point == 2
