import random


# 1) Add the class declaration. Use the following class comment.
class Deck:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
        x, y (int): The screen X and Y coordinates where the die will display.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self, param_x = 0, param_y = 0):
        """Constructs a new instance of Die with a value and points attribute. 
        Sets x,y to passed value, or 0,0 if none set.

        Args:
            self (Die): An instance of Die.
        """
        self.last_card = 0
        self.current_card = random.randint(1,13)

# 3) Create the roll(self) method. Use the following method comment.
    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)




    def display(self):

        print(self.current_card)
        return

