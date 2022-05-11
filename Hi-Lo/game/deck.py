import random


# 1) Add the class declaration. Use the following class comment.
class Deck:
    """A deck of cards that will generate a random card value, 1-13.

    The responsibility of Deck is to keep track of a card previously drawn and a new card drawn from the top of the deck. 
   
    Attributes:
        current_card (int): The currently drawn card.
        last_card (int): The previous card drawn.
        value (int): The value of the comparison between the two cards based on the user's choice.
    """

    def __init__(self):
        """Constructs a new instance of Deck with a current card attribute and a last card attribute. 

        Parameters:
            self (Deck): An instance of Deck.
        """
        self.last_card = 0
        self.current_card = random.randint(1,13)
        self.value = 0


    def calculate_draw(self, player_choice):
        """Calculates the point value of the current cards drawn based the user's choice.
        
        Parameters:
            self (Deck): An instance of Deck.
            player_choice (str): The choice the player made at some other point in the game.
        """
        self.value = -75  # Except for the conditions below, we assume a loss of points
        if  (player_choice == 'h') and (self.current_card > self.last_card) or \
            (player_choice == 'l') and (self.current_card < self.last_card):
            self.value = 100
        
        if (self.current_card == self.last_card):
            print("Aw, equal value is neither higher nor lower, which means you are wrong either way.")


    def draw(self):
        """Sets last_card as the value of the current card, then generates a new random value for current_card.
        
        Parameters:
            self (Deck): An instance of Deck.
        """
        print("\nDrawing a card...")
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)


    def show_cards(self):
        """Displays the value of the previous card (if there is one), and the value 
        of the current card. 

        Parameters:
            self (Deck): An instance of Deck.
        """
        print()
        if self.last_card > 0:
            print(f"The previous card was: {self.last_card}")
        print(f"The card now showing is: {self.current_card}")
