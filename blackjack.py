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
    if player_bank.balance <= 0:
        print("You are broke!")
        print("Balance:" + str(player_bank.balance))
        return False

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
    '''
        Hallitaan pelaajan käden tila.
        Jos yli palautetaan false ja jos 21 tai alle palautetaan true
       
    '''


    while True:
        print_hands_status(player_hand,dealer_hand)

        ## pelaaja ylitti rajan 21
        if player_hand.calculate_aces() > 21:
            break

        # Kysytään käyttäjältä haluaako nostaa lisää
        if not draw_more(player_hand):
            break
    return player_hand.calculate_aces() <= 21

def handle_dealer_hand(player_hand,dealer_hand):
    '''
        Hallitaan jakajan käden tila.
        Jos yli palautetaan false ja jos 21 tai alle palautetaan true
       
    '''
    
    while True:
        # Jos jakaja on yli
        if dealer_hand.calculate_aces() > 21:
            break
        
        # Jos jakajalla voittava käsi
        if dealer_hand.calculate_aces() >= player_hand.calculate_aces():
            break

        current_deck.draw(dealer_hand)

    return dealer_hand.calculate_aces() <= 21

def draw_more(hand):
    '''
        Kysytään käyttäjältä haluaako lisää kortteja vai ei 
    '''
    while True:
        answer = input("Do you wanna hit or stand (hit/stand)?")

        if answer.lower() == "hit":
            current_deck.draw(hand)
            return True
            break
        if answer.lower() == "stand":
            return False
            break

def print_hands_status(phand,dhand,show_all = False):
    '''
        printataan käsie tila
    '''

    print("Players hand:" + str(phand.calculate_aces()))
    for c in phand.current_cards:
        print(c)
    if not show_all:
        print("Dealers hand:")
        print(dhand.current_cards[0])
        print("One unidentified card")
    else:
        print("Dealer hand:" + str(dhand.calculate_aces()))
        print("Dealers hand:")
        for c in dhand.current_cards:
            print(c)

def player_wins():
    '''
    Hallitaan tilanne jossa pelaaja voittaa käden
    '''    
    print("You won " + str(player_bank.bet) + " moneys")
    player_bank.add_money(player_bank.bet)


def player_loses():
    '''
    Hallitaan tilanne jossa pelaaja häviää käden
    '''    
    print("You lost " + str(player_bank.bet) + " moneys")
    player_bank.remove_money(player_bank.bet)
    

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
        if handle_player_hand(player_hand,dealer_hand):
            ## palautus on true jos käsi on vielä 21 tai alle
            if player_hand.calculate_aces() == 21:
                ## Pelaaja voittaa
                print("x1")
                player_wins()
                print_hands_status(player_hand,dealer_hand,True)
            elif handle_dealer_hand(player_hand,dealer_hand):
                ##Pelaaja on hävinnyt
                player_loses()
                print("x2")
                print_hands_status(player_hand,dealer_hand,True)
            else:
                ## Pelaaja voittaa koska jakaja meni yli
                player_wins()
                print("x3")
                print_hands_status(player_hand,dealer_hand,True)


        else:
            ## peli on jo hävitty
            player_loses()
            print("x4")
            print_hands_status(player_hand,dealer_hand,True)
  

    else:
        print("Exit Game")
        break
