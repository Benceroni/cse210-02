from re import S
from game.deck import Deck  

"""NOTE:
Our team did not get to the point of delegation before our team meeting had to end. 

We each decided to create our own branch and try creating the program on our own and, 
compare each other's solutions.

I worked on my program for about three hours, troubleshot it for another 90 minutes, and 
ran out of time to keep working on it.

At that point, I compared my solution to another team member's solution and studied the 
differences to see how/why/where mine had failed.

I identified the most with Dallas's solution as it was similar to mine and I understand
why his works.
""" 

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play and keep track of the score.

    Attributes:
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        
        deck = Deck()

        self.is_playing = True
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Present a card and ask the user for their guess.

        Args:
            self (Director): An instance of Director.
        """
        last_card1 = Deck.draw(self).last_card
        print(f"The card is: {last_card1}")

        guess = input("Higher or lower? [h/l] ")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        current_card1 = Deck.draw.current_card

        print(f"Next card was: {current_card1}")


    def do_outputs(self):
        """Displays the total_score and determines if the game is still playing. Also asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        if self.get_inputs.guess == "l":
            if self.get_inputs.last_card1 > self.do_outputs.current_card1:
                self.score += 100
            else:
                self.score -= 75
        else:
            if self.get_inputs.last_card1 < self.do_outputs.current_card1:
                self.score += 100
            else:
                self.score -= 75

        print(f"Your score is: {self.score}")

        self.is_playing == (self.score > 0)

        if self.score <= 0:
            self.is_playing = False
            print("Game Over.")
        else:
            game_status = input("Play again? [y/n] ")

            if game_status == "y":
                self.is_playing = True
            else:
                self.is_playing = False
                print("Thanks for playing!")