import random


#need to create csv for wallet  

def title():
    print("BLACKJACK!")
    
    print("Blackjack payout is 3:2")
    print()

def create_deck(deck):
    suit = ["C", "D", "H", "S"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    for s in suit:
        for i in range (len(rank)):
            card = [rank[i], s, value[i]]
            deck.append(card)
    return deck
                



def shuffle_deck(deck):
    random.shuffle(deck)


def initial_deal(deck,deck2):
    card = deck.pop()
    deck2.append(card)
    card = deck.pop()
    deck2.append(card)
    return deck2

def check_score(hand):
    score = 0
    for value in hand:
        score += value[2]
    return score
        
    
    


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


        player_hand = initial_deal(deck, player_hand)
        house_hand = initial_deal(deck, house_hand)
        
        print("DEALER'S SHOW CARD:")
        print(house_hand)
        print()
        print("Your Cards:")

        print(player_hand)
        score = check_score(player_hand)
        print(f"Current score: {score}")
        print(f"{len(player_hand)} cards")
        print(f"{len(deck)} cards")
        #print(check_score(player_hand))
    

        while True:
            choice = input("Hit or stand? (hit/stand):").lower()
            if choice == "hit":
                player_hand.append(deck.pop())
                print(f" {len(player_hand)} cards")
                print(f" {len(deck)} cards")
                continue
            else:
                break
                
        

        






        choice3 = input("Go again? (y/n): ")
        if choice3 == "n":
            print()
            print("Bye")
            break


if __name__ == "__main__":
    main()
