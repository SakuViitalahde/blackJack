import card
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Deck:

    def __init__(self):
        self.used_deck = []
        self.shuffle()
    
    def __str__(self):
        return "You have " + str(len(self.used_deck)) + "left"

    def shuffle(self):
        for suit in suits:
            for rank in ranks:
                self.used_deck.append(card.Card(rank,suit, values[rank]))
        random.shuffle(self.deck)  
    
    def deal(self, hand):
        hand.append(self.draw())
        hand.append(self.draw())
        
    def draw(self):
        return self.used_deck.pop()

    