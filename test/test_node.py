from labyrinth.node import Node
from labyrinth.element import Element


def test_is_equal_to():
    """Test the method Node.is_equal_to(other_node)"""

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(1)
    not_equal = node_1.is_equal_to(node_2)
    nodes_equal = node_1.is_equal_to(node_3)
    assert not_equal == False
    assert nodes_equal == True



def test_set_connected_to():
    """Test the methode Node.set_connected_to(other_node)"""

    node_1 = Node(1)
    node_2 = Node(2)
    node_1.set_connected_to(node_2)
    assert node_1.connected_to == [node_2]



def test_set_list_elements():
    """Test the method Node.set_list_elements(element) """

    node_1 = Node(1)
    node_2 = Node(2)
    element_1 = Element("Mur", "X", True)
    element_2 = Element("Bouton", "B", False)
    node_1.set_list_elements(element_1)
    node_2.set_list_elements([element_1, element_2])

    assert node_1.list_elements == [element_1]
    assert node_2.list_elements == [element_1, element_2]
    
