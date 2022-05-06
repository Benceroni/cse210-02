import random


# 1) Add the class declaration. Use the following class comment.
class Deck:
    """A deck of cards that will generate a random card value, 1-13.

    The responsibility of Deck is to keep track of a card previously drawn and a new card drawn from the top of the deck. 
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
        x, y (int): The screen X and Y coordinates where the die will display.
    """

    def __init__(self):
        """Constructs a new instance of Deck with a current card attribute and a last card attribute. 

        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = 0
        self.current_card = random.randint(1,13)


    def draw(self):
        """Puts the current value of the card as the 'old value', then generates a new random value.
        
        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)


    def display(self):

        print(self.current_card)
        return

