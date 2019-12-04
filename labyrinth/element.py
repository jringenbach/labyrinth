class Element:



    def __init__(self, name, symbol, block_agent):
        """
        self.name (str) : name of the element
        self.symbol (str) : symbol of the element
        self.block_agent (bool) : determine if it blocks the agent trying to escape the labyrinth or not"""

        self.name = name
        self.symbol = symbol
        self.block_agent = block_agent



    def about_me(self):
        """Print on the terminal every information about this Element Object"""

        print("Name : "+self.name)
        print("Symbol : "+self.symbol)
        print("Block the agent : "+self.block_agent)



    def is_equal_to(self, another_element):
        """Test if this element is equal to another Element Object. Return True if it is, False else.
        
        another_element (Element) : Element object """

        #If the elements have the same name, same symbol, and block the agent in the same way
        if self.name == another_element.name and \
        self.symbol == another_element.symbol and \
        self.block_agent == another_element.block_agent:
            return True
        
        else:
            return False