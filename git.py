import random
import time


#need to create csv for wallet  

def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("House stands at 16")
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


def first_deal(deck,hand):
    card = deck.pop()
    hand.append(card)
    return hand

def add_score(hand):
    score = 0
    ace = 0
    
    for value in hand:
        score += value[2]
        if value[2] == 11:
            ace += 1
    #ace handling 
    if score > 21 and ace > 0:
        score -= 10
        ace -= 1
    return score

#to confirm if ace is in hand
def check_ace(hand):
    for value in hand:
        if value[2] == 11:
            return True
    return False
    
    


def main():
    title()
    
    while True:
        #print(f"Money: {bank}")
        #bet = float(input(f"Bet: "))
        
        deck = []
        player_hand = []
        house_hand = []
        
        create_deck(deck)
        shuffle_deck(deck)

        #Initial deal
        player_hand = first_deal(deck, player_hand)
        house_hand = first_deal(deck, house_hand)
        player_hand = first_deal(deck, player_hand)
        house_hand = first_deal(deck, house_hand)


        print("DEALER'S SHOW CARD:")
        print(house_hand[0])
        house_score = add_score(house_hand)
        print()
        print("Your Cards:")
        print(player_hand)
        player_score = add_score(player_hand)
        print(f"Your Score: {player_score}")
        ace = check_ace(player_hand)
        print(f"Ace?: {ace}")
        if player_score == 21:
            print(f"BLACKJACK!!! Your score: {player_score}")
            continue

        print()
        
        #player choice
        while True:
            choice = input("Hit or stand? (hit/stand): ").lower()
            if choice == "hit":
                player_hand.append(deck.pop())
                player_score = add_score(player_hand)
                print(player_hand)
                print(f"Your Score: {player_score}")
                ace = check_ace(player_hand)
                print(f"Ace?: {ace}")
                if player_score > 21:
                    print(f"BUST! You Lose.")
                    print()
                    break
                elif player_score == 21:
                    print(f"BLACKJACK!!! Your score: {player_score}")
                    print()
                    break
                continue
            elif choice == "stand":
                break

            
        #house turn
        if player_score < 21:
            print()
            print("House Turn")
            print()
            print("flipping card...")
            print()
            time.sleep(1)
            print(house_hand)
            house_score = add_score(house_hand)
            print(f"House Score: {house_score}")

            #While house has a score less than 16 they must hit   
            while house_score < 16:
                print("House draws another card")
                time.sleep(2)
                house_hand.append(deck.pop())
                house_score = add_score(house_hand)
                print(house_hand)
                print(f"House Score: {house_score}")

            #final check of house outcome        
            if house_score > 21:
                print(f"BUST! House score: {house_score}")
                print()
                print("You Win!")
                
            elif house_score == 21:
                print(f"BLACKJACK!!! House score: {house_score}")
                print()
                print("House Wins!")
                
            elif house_score > player_score:
                print("House wins!")
                print()
                
            elif house_score < player_score:
                print("You Win!")
                print()
                
            else:
                print("PUSH")
                
            
        

                
        #Continue game?
        choice3 = input("Go again? (y/n): ")
        if choice3 == "y":
            print()
            print("shuffling cards...")
            print()
            time.sleep(1)
        if choice3 == "n":
            print()
            print("Bye")
            break


if __name__ == "__main__":
    main()
