import random

class Deck:
    """A random deck of cards with values of 1 to 13.

    The responsibility of the Deck is to keep track of the current and last card that were drawn.
   
    Attributes:
        last_card (int): The last card that was played.
        current_card (int): The current card of the deck.
        value (int): The value of the current card being displayed.
    """

    def __init__(self):
        """Constructs a new instance of Deck with a last_card and current_card attribute. 

        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = 0
        self.current_card = random.randint(1,13)
        self.value = 0

    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Deck): An instance of Deck.
        """
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)

    def calculate_value(self, player_choice):
        """Calculates the value of the inmediate card

        Args:
            self (Deck): An instance of Deck.
            player_choice: The guess of the player(h or l).
        """

        if self.last_card >= self.current_card and player_choice == "l" \
        or self.last_card <= self.current_card and player_choice == "h":
            self.value = 100
        else: self.value = -75