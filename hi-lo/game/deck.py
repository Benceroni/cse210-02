import random


# 1) Add the class declaration. Use the following class comment.
class Deck:
    """A random deck of cards with values of 1 to 13.

    The responsibility of the Deck is to keep track of the current and last card that were drawn.
   
    Attributes:
        last_card (int): The last card that was played.
        current_card (int): The current card of the deck.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Deck with a last_card and current_card attribute. 

        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = 0
        self.current_card = random.randint(1,13)

# 3) Create the draw(self) method. Use the following method comment.
    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)