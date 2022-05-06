import random

class Deck:
    
    def __init__(self):
        self.current_card = 0
        self.last_card = 0

    def draw_card(self):
        self.last_card = self.current_card
        self.current_card = random.randint(1,14)

