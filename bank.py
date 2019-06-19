class Bank:
    '''
        Pelaajan kanssan hallinta luokka
    '''
    def __init__(self):
        self.balance = 50
        self.bet = 0
    
    def add_money(self,amount):
        '''
            Lisätään pelaajalle rahaa
        '''
        self.balance = self.balance + amount

    def remove_money(self,amount):
        '''
            Vähennetään pelaajalta rahaa pelaajalle rahaa
        '''
        self.balance = self.balance - amount