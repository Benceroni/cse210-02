import random


# 1) Add the class declaration. Use the following class comment.
class Deck:
    """A deck of cards that will generate a random card value, 1-13.

    The responsibility of Deck is to keep track of a card previously drawn and a new card drawn from the top of the deck. 
   
    Attributes:
        current_card (int): The currently drawn card.
        last_card (int): The previous card drawn.
    """

    def __init__(self):
        """Constructs a new instance of Deck with a current card attribute and a last card attribute. 

        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = 0
        self.current_card = random.randint(1,13)


    def draw(self):
        """Sets last_card as the value of the current card, then generates a new random value for current_card.
        
        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)

