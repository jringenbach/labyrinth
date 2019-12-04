from labyrinth.element import Element

def test_is_equal_to():
    """Test the method Element.is_equal_to(another_element)"""
    element_to_test = Element("Agent", "A", False)
    element_1 = Element("Agent", "A", False)
    element_2 = Element("Wall", "X", True)

    assert element_to_test.is_equal_to(element_1) == True
    assert element_to_test.is_equal_to(element_2) == False