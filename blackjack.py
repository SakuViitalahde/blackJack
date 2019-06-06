import bank
import deck
import hand

'''
    Peli itsessään
'''
player_bank = bank.Bank()
current_deck = deck.Deck()

def ask_bet():
    '''
        Kysytään halutaanko pelata
    '''
    while True:
        answer = input("Do you wanna play more (y/n)?")

        if answer.lower() == "y":
            return True
            break
        if answer.lower() == "n":
            return False
            break

def ask_amount():
    '''
        Kysytään paljonko halutaan pelata
    '''
    while True:
        try:
            print("Current balance is:" + str(player_bank.balance))
            answer = int(input("How much you wanna bet?"))
            return answer
        except:
            print("not valid value")
        else:            
            break

def handle_player_hand(player_hand,dealer_hand):
    while True:
        print_hands_status(player_hand,dealer_hand)

        if not draw_more(player_hand):
            break

def draw_more(hand):
    while True:
        answer = input("Do you wanna hit or stand (hit/stand)?")

        if answer.lower() == "hit":
            current_deck.draw(hand)
            return True
            break
        if answer.lower() == "stand":
            return False
            break

def print_hands_status(phand,dhand):
    '''
        printataan käsie tila
    '''

    print("Pelaajan käsi:" + str(phand.value))
    for c in phand.current_cards:
        print(c)
    
    print("Jakajan käsi:")
    print(dhand.current_cards[0])
    print("Yksi tuntematon kortti")

## Game loop
while True:
    if ask_bet():
        player_bank.bet = ask_amount()

        ## Luodaan uudet kädet
        player_hand = hand.Hand()
        dealer_hand = hand.Hand()

        #Jaetaan uudet kädet uudet kädet
        current_deck.deal(player_hand)
        current_deck.deal(dealer_hand)

        # pelaajan pelin oma looppi (hit/stand)
        handle_player_hand(player_hand,dealer_hand)
  

    else:
        print("Exit Game")
        break
