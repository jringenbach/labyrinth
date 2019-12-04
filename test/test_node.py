from labyrinth.node import Node
from labyrinth.element import Element



def test_find_element():
    """Test the method Node.find_element(element_to_find)"""

    element_1 = Element("Start", "S", False)
    element_2 = Element("Agent", "A", False)
    node_to_test = Node(1, (0,0), elements=[element_1, element_2])
    element_found = node_to_test.find_element(element_2)

    assert element_found == element_2



def test_find_element_by_parameter():
    """Test the method Node.find_element_by_parameter(parameter, value)"""

    element_1 = Element("Start", "S", False)
    element_2 = Element("Agent", "A", False)
    node_to_test = Node(1, (0,0), elements=[element_1, element_2])
    element_found = node_to_test.find_element_by_parameter(parameter="name", value="Agent")
    element_found_2 = node_to_test.find_element_by_parameter(parameter="symbol", value="S")

    assert element_found == element_2
    assert element_found_2 == element_1



def test_is_equal_to():
    """Test the method Node.is_equal_to(other_node)"""

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(1)
    nodes_not_equal = node_1.is_equal_to(node_2)
    nodes_equal = node_1.is_equal_to(node_3)
    assert nodes_not_equal == False
    assert nodes_equal == True


def test_remove_element():
    """Test the method Node.remove_element(element_to_remove) where an element must be remove from the 
    list of elements attribute in the Node"""

    element_to_remove = Element("A", "Agent", False)
    node = Node(1, (0,0), elements=[element_to_remove])
    node.remove_element(element_to_remove)

    assert len(node.elements) == 0



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
    
