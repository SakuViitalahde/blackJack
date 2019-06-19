class Card:
    '''
        Kortti luokka kortin tulostusta ja arvojen tilan säilytystä varten
    '''
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        '''
            Paluttaa kortit tiedot luettavassa muodossa
        '''
        return self.suit + " : " + self.rank + " : " + str(self.value)