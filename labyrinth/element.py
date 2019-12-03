class Element:

    def __init__(self, name, symbol, block_agent):
        """
        self.name (str) : name of the element
        self.symbol (str) : symbol of the element
        self.block_agent (bool) : determine if it blocks the agent trying to escape the labyrinth or not"""

        self.name = name
        self.symbol = symbol
        self.block_agent = block_agent