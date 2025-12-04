import random
import time


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


def first_deal(deck,hand):
    card = deck.pop()
    hand.append(card)
    return hand

def add_score(hand):
    score = 0
    for value in hand:
        score += value[2]        
    return score

#check_ace for ace handling
def check_ace(hand):
    for value in hand:
        if value == 11:
            return True
    return False
    
    


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

        #initial deal
        player_hand = first_deal(deck, player_hand)
        house_hand = first_deal(deck, house_hand)
        player_hand = first_deal(deck, player_hand)
        house_hand = first_deal(deck, house_hand)

        print(f"{len(player_hand)} cards")
        print(f"{len(deck)} cards left")
        print()
        print("DEALER'S SHOW CARD:")
        print(house_hand[0])
        house_score = add_score(house_hand)
        print()
        print("Your Cards:")
        print(player_hand)
        player_score = add_score(player_hand)
        print(f"Your Score: {player_score}")
        print()
        
        #Choice
        while True:
            choice = input("Hit or stand? (hit/stand): ").lower()
            if choice == "hit":
                player_hand.append(deck.pop())
                player_score = add_score(player_hand)
                print(player_hand)
                print(player_score)
                if player_score > 21:
                    print(f"BUST! Your score: {player_score}")
                    break
                elif player_score == 21:
                    print(f"BLACKJACK!!! Your score: {player_score}")
                    break
                continue
            elif choice == "stand":
                break
            
        #house turn
        print("House Turn")
        print()
        house_score = add_score(house_hand)
        print("flipping card...")
        time.sleep(2)
        print(house_hand)
        print(f"House Score: {house_score}")
        time.sleep(2)
        if house_score < 16:
            while True:
                    house_hand.append(deck.pop())
                    house_score = add_score(house_hand)
                    print(house_hand)
                    print(house_score)
                    if house_score > 21:
                        print(f"BUST! House score: {house_score}")
                        print("You Win!")
                        break
                    elif house_score == 21:
                        print(f"BLACKJACK!!! House score: {house_score}")
                        print("You lose!")
                        break
                

        
    
            
        '''#house is to hit until > 1
            if player_score >= 21:
                break
            else:
                while True:
                    house_score = add_score(house_hand)
                    if house_score < 17:
                        house_hand.append(deck.pop())
                        continue
                    elif house_score == 21:
                        print(f"BLACKJACK!!! House Wins!")
                        break        
        




        
                if player_score > 21:
                    print(f"BUST! Your score: {player_score}")
                    break
                elif player_score == 21:
                    print(f"BLACKJACK!!! Your score: {player_score}")
                    break
            elif choice == "stand":
                print(player_hand)
                player_score = add_score(player_hand)
                break
            else:
                print("Invalid choice. hit/stand?")


        





        
        

        player_score = add_score(player_hand)
        print(f"Current score: {house_score}\n")
        player_score = add_score(player_hand)
        if player_score == 21:
            print(f"BLACKJACK!!! Your score: {player_score}")
            break
        
        ace = check_ace(player_hand)
        print(ace)
        print(f"Current score: {player_score}")
        print()
        print(f"{len(player_hand)} cards")
        print(f"{len(deck)} cards left")
        
    
        #hit/stand
        while True:
            choice = input("Hit or stand? (hit/stand): ").lower()
            if choice == "hit":
                player_hand.append(deck.pop())
                print(player_hand)
                player_score = add_score(player_hand)
                if player_score > 21:
                    print(f"BUST! Your score: {player_score}")
                    break
                elif player_score == 21:
                    print(f"BLACKJACK!!! Your score: {player_score}")
                    break
            elif choice == "stand":
                print(player_hand)
                player_score = add_score(player_hand)
                break
            else:
                print("Invalid choice. hit/stand?")
            
        #house is to hit until > 1
        while True:
            house_score = add_score(house_hand)
            if house_score < 17:
                house_hand.append(deck.pop())
                continue
            elif house_score == 21:
                print(f"BLACKJACK!!! House Wins!")
                break'''
                

        choice3 = input("Go again? (y/n): ")
        if choice3 == "n":
            print()
            print("Bye")
            break


if __name__ == "__main__":
    main()
