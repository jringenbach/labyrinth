from labyrinth.node import Node
from labyrinth.element import Element



def test_connected_to_is_equal():
    """Test the method Node.connected_to_is_equal(another_node)"""

    #We create our test nodes
    node_1 = Node(1, (1,0))
    node_2 = Node(2, (1,1))
    node_3 = Node(3, (1,2))
    node_4 = Node(4, (1,1))
    node_5 = Node(5, (0,1))

    #We set the connection between the nodes
    node_1.connected_to = [node_2]
    node_2.connected_to = [node_1, node_3]
    node_3.connected_to = [node_2]
    node_5.connected_to = [node_4]

    assert node_1.connected_to_is_equal(node_3) == True
    assert node_2.connected_to_is_equal(node_1) == False #node_2.connected_to has more connexions than node_1
    assert node_1.connected_to_is_equal(node_5) == False #They are not connected to the same nodes



def test_find_element():
    """Test the method Node.find_element(element_to_find)"""

    element_1 = Element("Start", "S", False)
    element_2 = Element("Agent", "A", False)
    node_to_test = Node(1, (0,0), elements=[element_1, element_2])
    element_found = node_to_test.find_element(element_2)
    element_found_2 = node_to_test.find_element(element_1)

    assert element_found == element_2
    assert element_found_2 == element_1



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
    """Test the method Node.is_equal_to(another_node). They are equal if their num, position and nodes
    they are connected to are the same"""

    node_1 = Node(1, (0,0))
    node_2 = Node(2, (0,0))
    node_3 = Node(3, (1,1))
    node_4 = Node(1, (0,0))
    node_5 = Node(1, (1,2))
    node_6 = Node(6, (0,0))

    node_1.connected_to = [node_3]
    node_2.connected_to = [node_3]
    node_4.connected_to = [node_3]
    node_5.connected_to = [node_3]
    node_6.connected_to = [node_2, node_4]

    assert node_1.is_equal_to(node_2) == False #Their num is different
    assert node_1.is_equal_to(node_4) == True
    assert node_1.is_equal_to(node_5) == False #Position is different
    assert node_1.is_equal_to(node_6) == False #connected_to is different





def test_num_is_equal_to():
    """Test the method Node.is_equal_to(other_node)"""

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(1)
    nodes_not_equal = node_1.num_is_equal_to(node_2)
    nodes_equal = node_1.num_is_equal_to(node_3)

    assert nodes_not_equal == False
    assert nodes_equal == True



def test_position_is_equal_to():
    """Test the method Node.position_is_equal_to(another_node)"""

    node_1 = Node(1, (1,2))
    node_2 = Node(2, (1,2))
    node_3 = Node(3, (2,2))

    assert node_1.position_is_equal_to(node_2) == True
    assert node_1.position_is_equal_to(node_3) == False



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
    
