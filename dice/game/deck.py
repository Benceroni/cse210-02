import random


# 1) Add the class declaration.
class Deck:
    """A stack of individual cards. Each card contains a single value between 1-13 inclusive.

    The responsibliity of the Deck is to provide a Current Card value and to store the value of the Last Card played.
   
    Attributes:
        last_value (int): The number value of the last card played.
    """

# 2) Create the class constructor.
    def __init__(self):
        """Constructs a new instance of Deck with a Current Card attribute. 

        Args:
            self (Deck): An instance of Deck.
        """
        self.current_card = random.randint(1,13)

# 3) Create the draw(self) method.
    def draw(self):
        """Stores the new Last Card value and generates a new Current Card value.
        
        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)

