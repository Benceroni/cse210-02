from game.deck import Deck  

 
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deck : A deck of cards with 2 cards being recorded at the same time.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        num_Draws (int): The number of draws from the deck.
        hi_lo (string): Contains the response of the user.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.deck = Deck()
        self.is_playing = True
        self.score = 300
        self.num_draws = 0
        self.hi_lo = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.show_title()

        while self.is_playing:
            self.show_card()
            self.get_inputs()
            self.update_card()
            self.do_score()

    def show_title(self):
        """Shows a title screen and displays the rules of the game.
        
        Args:
            self (Director): an instance of Director.
        """
        print("\n--------------------------Hi-Lo--------------------------\n")
        print("The rules are simple. You will have a card and you will have to guess")
        print("if the next card is higher or lower than the current card. You start with 300 points.")
        print("If you guess right, 100 points more you will have.")
        print("If you guess wrong, 75 points you will lose. Don't get to 0 points or you'll lose!")

    def show_card(self):
        """Displays the current card.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing: return

        print(f"\nThe card is: {self.deck.current_card}")

    def get_inputs(self):
        """Ask the user if they want to draw.

        Args:
            self (Director): An instance of Director.
        """
        self.hi_lo = input("Higher or Lower? [h/l]: ").lower()
        while self.hi_lo != "h" and self.hi_lo != "l":
            self.hi_lo = input("I'm sorry, please confine your response to 'h' or 'l': ").lower()

    def update_card(self):
        """Updates the player's score and card.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing: return

        self.deck.draw()
        print(f"Next card was: {self.deck.current_card}")

        self.deck.calculate_value(self.hi_lo)
        self.num_draws += 1

    def do_score(self):
        """Shows the score and asks the user if they want to keep playing.

        Args:
            self (Director): an instance of Director.
        """
        self.score += self.deck.value
        print(f"Your score is: {self.score}")
        self.is_playing = (self.score > 0)
        if self.score <= 0:
            self.end_game()

        if not self.is_playing: return

        keep_playing = input("Play again? [y/n]: ").lower()
        while keep_playing != "y" and keep_playing != "n":
            keep_playing = input("I'm sorry, please confine your response to 'n' or 'y': ").lower()
        
        if keep_playing == "n":
            self.end_game()

    def end_game(self):
        """Provides a clean exit to the game by printing the final score and saying goodbye.
        
        Args:
            self (Director): an instance of Director.
        """
        print()
        if self.score <= 0:  #The player lost all their points.
            print("Seems like your luck ran out.")
        else:   # Or the player must have chosen to quit.
            print("You know there's no risk to keep drawing, right? Oh well...")

        print(f"You ended up with {self.score} points in the card number {self.num_draws}.")
        print("Thank you for playing! Goodbye!\n")
        self.is_playing = False
        return