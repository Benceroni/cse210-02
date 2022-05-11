from game.deck import Deck 
from game.player import Player 
 
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deck : A single Deck instance.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        num_guesses (int): The number of guesses attempted by the player.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Parameters:
            self (Director): an instance of Director.
        """
        self.deck = Deck()
        self.player = Player("Player", 300)


    def show_title(self):
        """Shows a title screen and displays the rules of the game.
        
        Parameters:
            self (Director): an instance of Director.
        """
        print("\33[2J\33[H")    # Clear/Home Screen
        print("HI-LO\n")
        print("The rules are simple. You will start with 300 points. I will draw a card ")
        print("from the deck and show it to you. Your job is to decide if the next cars is")
        print("(H)igher or (L)ower than the card currently shown.\n")
        print("I will draw the next card. If you are correct, you win 100 points.")
        print("If you are incorrect, you will lose 75 points.\n")
        print("After each card drawn, you will have the option to quit and keep your score,")
        print("but if you run out of points, the game will be over.\n")


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Parameters:
            self (Director): an instance of Director.
        """
        self.show_title()

        while self.player.is_playing:
            self.deck.show_cards()
            self.ask_hi_lo()
            self.deck.draw()
            self.deck.show_cards()
            self.deck.calculate_draw(self.player.choice)    
            self.player.set_score(self.deck.value)
            self.player.show_score()
            self.ask_quit_game()

        self.do_end_game()


    def do_end_game(self):
        """Provides a clean exit to the game by printing the final score and saying goodbye.
        
        Parameters:
            self (Director): an instance of Director.
        """
        if self.player.score <= 0:  # Player ran out of points. (Possible to go negative.)
            print("Well, shoot... You ran out of points. Your streak is over.")
        else:   # Or the player must have chosen to quit.
            print("Ok, we will quit playing.")

        guess_word = "guess" if self.player.num_guesses == 1 else "guesses"

        print(f"You achieved a final score of {self.player.score} in {self.player.num_guesses} {guess_word}.\n")
        print("Thank you for playing! Goodbye!\n")


    def ask_quit_game(self):
        """Ask the user if they want to keep playing. Updates the is_playing attribute based
        on player's decision.

        Parameters:
            self (Director): An instance of Director.
        """
        # Make sure the player CAN still play before we ask... Player might have run out of points!
        if self.player.is_playing:
            prompt = "Would you like to keep playing?"
            self.player.make_choice(prompt)
            self.player.is_playing = (self.player.choice == 'y')
            print()


    def ask_hi_lo(self):
        """Ask the user to guess if the next card is higher or lower.

        Parameters:
            self (Director): An instance of Director.
        """
        prompt = "Do you think the next card is higher or lower?"
        valid_answers = ['h','l']
        self.player.make_choice(prompt, valid_answers)
 