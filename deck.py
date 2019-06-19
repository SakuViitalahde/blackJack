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
        '''
            Palauttaa korttien lukumäärän luettavassa muodossa
        '''
        return "You have " + str(len(self.used_deck)) + "left"

    def shuffle(self):
        '''
            Sekoittaa pakan uudelleen
        '''
        for suit in suits:
            for rank in ranks:
                self.used_deck.append(card.Card(rank,suit, values[rank]))
        random.shuffle(self.used_deck)  
    
    def deal(self, hand):
        '''
            Jakaa aloitus käden 2 kortti annetulle kädelle
        '''
        ## tarkitaan 2 kortti alkuun
        self.draw(hand)
        self.draw(hand)
        
    def draw(self,hand):
        '''
            nostaa kortin pakasta parametrina annetulle kädelle
        '''
        new_card = self.used_deck.pop()

        hand.current_cards.append(new_card)
        hand.value += new_card.value
        if new_card.rank == 'Ace':
            hand.aces += 1

    