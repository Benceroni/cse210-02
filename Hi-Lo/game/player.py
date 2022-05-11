class Player():
    """A player class to play the game with.
    
    Responsibilities: The player makes choices for the game. The player holds a score after being assigned points from the result of the game.
    
    Attributes:
        name (str): The name of the player.
        score (int): The current total score achieved by the player.
        choice: The choice of the player during the course of the game.
        is_playing: Whether or not the player is playing the game. 
        num_guesses: The number of guesses this player has attempted.

    """

    def __init__(self, name = "Player", score = 0):
        """A constructor to make a player.
        
        Parameters:
            self (Player): An instance of Player.
            name (str): An optinal name to be used, otherwise "Player".
            score (int): An optional starting score, otherwise 0.
        """
        self.name = name
        self.score = score
        self.choice = ''
        self.is_playing = True
        self.num_guesses = 0


    def show_score(self):
        """Displays the player's current score.
        
        Parameters:
            self (Player): An instance of Player."""
        print(f"{self.name}'s current score is: {self.score}")



    def set_score(self, value):
        """Adjusts the player's score by [value] number of points.
        
        Parameters:
            self (Player): An instance of Player.
            value (int): A point value to be added (or subtracted) from the player's score.
        """
        print()
        if value == 100:
            print("You won 100 points!")
        else:
            print("Aw... You lost 75 points.")
        print()
        self.score += value


    
    def make_choice(self, prompt, valid_answers = ['y','n']):
        """Allows the player to make a choice from a list of options.
        
        Parameters:
            self (Player): An instance of Player.
            prompt (str): A prompt to display to ask the user for a response.
            valid_answers (list[str]): A list of valid responses, in lowercase, accepted from the user."""
        valid_answer_str = str(valid_answers).replace("'","")
        user_choice = ''
        while user_choice not in valid_answers:
            user_choice = input(f"{prompt} {valid_answer_str}: ").lower()
            if user_choice not in valid_answers:
                print(f"\nPlease confine your answers to one of {valid_answer_str}.\n")
        
        self.choice = user_choice
        self.num_guesses += 1


