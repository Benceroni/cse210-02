from game.deck import Deck  
 
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
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
        


    def show_title(self):
        """Shows a title screen and displays the rules of the game.
        
        Args:
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
        
        Args:
            self (Director): an instance of Director.
        """
        self.show_title()

        while self.is_playing:
            self.show_card()
            a_guess = self.ask_hi_lo()
            self.update_card()
            self.show_card()
            self.do_score(a_guess)
            self.ask_quit_game()

        self.do_end_game()


    def do_end_game(self):
        """Provides a clean exit to the game by printing the final score and saying goodbye.
        
        Args:
            self (Director): an instance of Director.
        """
        print()
        if self.score <= 0:  # Player ran out of points. (Possible to go negative.)
            print("Well, shoot... You ran out of points. Your streak is over.")
        else:   # Or the player must have chosen to quit.
            print("Ok, we will quit playing.")

        draws = "draw" if self.num_draws == 1 else "draws"

        print(f"You achieved a final score of {self.score} in {self.num_draws} {draws}.\n")
        print("Thank you for playing! Goodbye!\n")


    def ask_quit_game(self):
        """Ask the user if they want to keep playing. Updates the is_playing attribute based
        on user's decision.

        Args:
            self (Director): An instance of Director.
        """
        # Make sure the player CAN still play before we ask... Player might have run out of points!
        if self.is_playing:
            valid_input = False   
            while not valid_input:
                user_response = input("Would you like to keep playing? [y/n]: ").lower()
                valid_input = user_response in ['y','n']
                if not valid_input:
                    print("I'm sorry, please confine your response to 'y' or 'n'.\n")

            self.is_playing = (user_response == 'y')
            print()


    def ask_hi_lo(self):
        """Ask the user to guess if the next card is higher or lower.

        Args:
            self (Director): An instance of Director.
        Returns:
            user_guess (str): The user's choice, either 'h' or 'l'. 
        """
        print()
        valid_input = False
        while not valid_input:
            user_guess = input("Next card higher or lower? [h/l]: ").lower()
            valid_input = user_guess in ['h','l']
            if not valid_input:
                print("I'm sorry, please confine your response to 'h' or 'l'.\n")
        print()
        return user_guess

 
    def update_card(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """

        self.deck.draw() 
        # Increase the number of rolls made.
        self.num_draws += 1


    def show_card(self):
        """Displays the current value of the card. 

        Args:
            self (Director): An instance of Director.
        """
        
        if self.deck.last_card > 0:
            print(f"The previous card was: {self.deck.last_card}")
        print(f"The card now showing is: {self.deck.current_card}")


    def do_score(self, guess):
        """Checks the users guess against the evaluation of the two cards and determines 
        a win or a loss of points. Notifies the user """
        print()

        if  (guess == 'h' and self.deck.current_card > self.deck.last_card) or \
            (guess == 'l' and self.deck.current_card < self.deck.last_card):
            self.score += 100
            print("You won 100 points!")
        else:
            if (self.deck.current_card == self.deck.last_card):
                print("Equal value? Well, you weren't wrong, but more importantly: You weren't right, either.")
            self.score -= 75
            print("You lost 75 points...")

        print(f"Your current score is:\t{self.score}\n".expandtabs(25))
        self.is_playing = (self.score > 0)