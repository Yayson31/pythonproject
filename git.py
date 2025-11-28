import random

def title():
    print("BLACKJACK!")
    
    print("Blackjack payout is 3:2")
    print()

def create_deck(deck):
    suit = ["C", "D", "H", "S"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    for s in suit:
        for r in rank:
            deck.append(r+s)



def shuffle_deck(deck):
    random.shuffle(deck)


def card_deal(deck,deck2):
    card = deck.pop()
    deck2.append(card)
    card = deck.pop()
    deck2.append(card)
    return deck2

'''def play_game(deck):'''
    
    


def main():
    title()
    
    while True:
        #print(f"Money: {bank}")
        #bet = float(input(f"Bet: "))
        print()
        
        deck = []
        player_hand = []
        house_hand = []
        
        create_deck(deck)
        shuffle_deck(deck)

        player_hand = card_deal(deck, player_hand)
        house_hand = card_deal(deck, house_hand)
        
        print(f"DEALER'S SHOW CARD:\n{house_hand[0]}")
        print()
        print(f"Your Cards:\n{player_hand}")
        print()
    
        
        print(len(deck))
        print(deck)

        '''player_card = deck.pop()
        player_card = deck.pop()
        house_card = deck.pop()
        player_hand.append(play_card)
        player_hand.append(play_card)
        player_hand.append(play_card)'''
        
        

        '''cpu_card1 = random.choice(deck)
        player_card2 = random.choice(deck)
        cpu_card2 = random.choice(deck)'''
        

        '''print(f"DEALER'S SHOW CARD:\n{cpu_card1}")
        print()
        print(f"Your Cards:\n{player_card1}\n{player_card2}")
        print()

        while True:
            choice = input("Hit or stand? (hit/stand):").lower()
            if choice == "hit":
                player_card3 = random.choice(deck)
                print(player_card3)
                continue
            else:
                break'''
                
        

        






        choice3 = input("Go again? (y/n): ")
        if choice3 == "n":
            print()
            print("Bye")
            break


if __name__ == "__main__":
    main()
