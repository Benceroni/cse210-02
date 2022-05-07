from game.deck import Deck

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
        
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.game_deck = Deck()
        self.turn = 0
        self.response = ''
        self.answer = ''
        self.score = 300


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.game_deck.draw_card()

        while self.is_playing:
            self.turn += 1
            self.get_inputs()
            self.game_deck.draw_card()
            self.do_checks()
            self.do_output()


    def get_inputs(self):
        """Ask the user if card is higher or lower

        Args:
            self (Director): An instance of Director.
        """
        print(f"\nThe card is {self.game_deck.current_card}")
        self.response = input("Higher, lower, or same? (high/low/same): ")


    def do_checks(self):
        """Determine the correct choice, and check to see if the choice is correct.

        Args:
            self (Director): An instance of Director.
        """
        if self.game_deck.last_card > self.game_deck.current_card:
            self.answer = 'low'
        elif self.game_deck.last_card < self.game_deck.current_card:
            self.answer = 'high'
        elif self.game_deck.last_card == self.game_deck.current_card:
            self.answer = 'same'

        if self.response != self.answer:
            self.score -= 75
        elif self.response == self.answer:
            self.score += 100
        
        if self.score <= 0:
            self.is_playing = False

    def do_output(self):
        """ Outputs current card, handles scoring, and asks player if they want
            to continue

        Args:
            self (Director): An instance of Director.
        """
        print(f"Next card was {self.game_deck.current_card}")
        print(f"Your score is { self.score }")

        keep_playing = ''

        if self.is_playing:
            keep_playing = input(f"Play again? [y/n]: ")
            if keep_playing != 'y':
                self.is_playing = False


