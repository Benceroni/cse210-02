# from game.deck import Deck
from game.director import Deck

class Player:
    """A player who will keep track of the score.

    The responsibility of Player is to keep track of the score.
   
    Attributes:
        score (int): The player's current score.
    """

    def __init__(self):
        """Constructs a new instance of Player with a score. 

        Args:
            self (Player): An instance of Player.
        """
        self.score = 300
        # self.deck = Deck()


    def do_score(self, guess, current_card, last_card):
        """Updates the score of the game based on the result of the last guess.
        
        Args:
            self (Player): An instance of Player.
            guess (string): Input from Director.
            current_card (int): Newly turned pver card from Director.
            last_card (int): Card that was showing before guess from Director.
        """

        if  (guess == 'h' and current_card > last_card) or \
            (guess == 'l' and current_card < last_card):
            # If the player's guess matches the relation of the two cards, they win points.
            self.score += 100
            print("You won 100 points!")
        else:
            # Otherwise, they lose points.
            if (current_card == last_card):
                print("Equal value? Well, you weren't wrong, but more importantly: You weren't right, either.")
            self.score -= 75
            print("You lost 75 points...")

        # Print the score and determine if the player is able to continue playing.
        print(f"Your current score is:\t{self.score}\n".expandtabs(25))
        self.is_playing = (self.score > 0)