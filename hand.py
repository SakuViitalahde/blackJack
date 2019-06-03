class Hand:
    '''
        Luokka käsien hallintaan
    '''
    def __init__(self):
        self.current_cards = []
        self.value = 0 
        self.aces = 0
    
    def add_card(self,card):
        self.current_cards.append(card)
    
    def calculate_aces(self):
        pass