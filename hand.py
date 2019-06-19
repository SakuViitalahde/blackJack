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
        '''
            Palauttaa ässillä lasketun lähimmän arvon joka ei ole kuitenkaan yli 21
        '''
        if self.aces > 0:
            num = self.value
            for x in range(self.aces):
                num = num - 10
                if self.value > 21 and num <= 21:
                    return num
            return self.value
        else:
            return self.value
                    



