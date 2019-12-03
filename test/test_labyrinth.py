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


def test_equals_list_nodes():
    """Test the method Labyrinth.equals_list_nodes()"""

    #We create our labyrinth that will calculate connections between its nodes
    lab = Labyrinth()
    lab.labyrinth = [["X", "X", "X"], ["", "", ""], ["X","X", "X"]]
    lab.set_list_nodes_from_labyrinth()
    lab.set_connection_between_nodes()

    #We set custom nodes with their connections between them
    node_1 = Node(1, (1,0))
    node_2 = Node(2, (1,1))
    node_3 = Node(3, (1,2))
    node_1.connected_to = [node_2]
    node_2.connected_to = [node_1, node_3]
    node_3.connected_to = [node_2]
    list_nodes = [node_1, node_2, node_3]
    list_nodes_2 = [node_1, node_2]

    #We test if the two lists of nodes are equal
    assert lab.equals_list_nodes(list_nodes) == True
    assert lab.equals_list_nodes(list_nodes_2) == False



def test_get_labyrinth_from_file_name():
    """Test the method Labyrinth.get_labyrinth_from_file_name"""

    lab = Labyrinth(file_name="test/test_model_labyrinth/lab.xls")
    labyrinth_to_test = [["X", "X", "X"], ["X", "", "X"], ["X","X", "X"]]
    assert lab.labyrinth == labyrinth_to_test



def test_set_connection_between_nodes():
    """Test the method Labyrinth.get_connection_between_nodes()"""

    #Labyrinth on which we will test our method set_connection_between_nodes
    lab = Labyrinth()
    lab.labyrinth = [["X", "", "X"], ["", "", ""], ["X","", "X"]]
    lab.set_list_nodes_from_labyrinth()
    lab.set_connection_between_nodes()

    #We create our nodes for the test
    node_1 = Node(1, (0,1))
    node_2 = Node(1, (1,0))
    node_3 = Node(1, (1,1))
    node_4 = Node(1, (1,2))
    node_5 = Node(1, (2,1))

    #We create the connections between our test nodes
    node_1.connected_to = [node_3]
    node_2.connected_to = [node_3]
    node_3.connected_to = [node_1, node_2, node_4, node_5]
    node_4.connected_to = [node_3]
    node_5.connected_to = [node_3]
    list_nodes_test = [node_1, node_2, node_3, node_4, node_5]

    lab.set_connection_between_nodes()
    assert lab.equals_list_nodes(list_nodes_test) == True


def test_set_list_of_nodes_from_labyrinth():
    """Test the method Labyrinth.set_list_of_nodes_from_labyrinth()"""

    lab = Labyrinth()
    lab.labyrinth = [["X", "X", "X"], ["X", "", "X"], ["X","X", "X"]]
    lab.set_list_nodes_from_labyrinth()
    node_1 = Node(1, (1,1))

    assert lab.list_nodes[0].num == node_1.num and lab.list_nodes[0].labyrinth_position == node_1.labyrinth_position