import random
import time
import db


#Money system in db module
#title
def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("House stands at 17")
    print("Cards read as follow: Rank, suit, value")
    print("C = Clubs, D = Diamonds, H = Hearts, S = Spades")
    print()

#create deck
def create_deck(deck):
    suit = ["C", "D", "H", "S"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    for s in suit:
        for i in range (len(rank)):
            card = [rank[i], s, value[i]]
            deck.append(card)
    return deck
            
#shuffle deck
def shuffle_deck(deck):
    random.shuffle(deck)

#first deal 
def first_deal(deck,hand):
    card = deck.pop()
    hand.append(card)
    return hand

#split add score function for each hand
def add_player_score(hand):
    score = 0
    ace = 0
    
    for value in hand:
        if value[2] == 11:
            if score + 11 > 21:
                score += 1
            else:
                # Give player the choice
                choice = input("You drew an Ace! Count as 1 or 11? ")
                if choice.strip() == "11":
                    score += 11
                else:
                    score += 1
            ace += 1
        else:
            score += value[2]
    #ace handling
    while score > 21 and ace > 0:
        score -= 10
        ace -=1
    
    return score


def add_house_score(hand):
    score = 0
    ace = 0
    
    for value in hand:
        score += value[2]
        if value[2] == 11:
            ace += 1
    #ace handling 
    while score > 21 and ace > 0:
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
        #load wallet
        wallet = db.load_wallet()
        print(f"Your current balance: ${wallet:.2f}")

        # Ask for bet
        while True:
            try:
                bet = float(input("Enter your bet: "))
                if bet <= 0:
                    print("Bet must be greater than 0.")
                elif bet > wallet:
                    print("Not enough funds!")
                    option = input("Buy $100 worth of chips? (y/n): ")
                    if option == "y":
                        chips = 100.00
                        wallet = db.add_money(wallet, chips)
                        print(f"Your current balance: ${wallet:.2f}")
                elif bet < 5 or bet > 1000:
                    print("Min bet is $5. Max bet is $1000.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        # Deduct bet
        wallet = db.bet_money(wallet, bet)
        print(f"Bet placed: ${bet:.2f}.\nRemaining balance: ${wallet:.2f}")
        print()
        
        #create deck and hands and shuffle deck
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
        house_score = add_house_score(house_hand)
        print()
        print("Your Cards:")
        print(player_hand)
        player_score = add_player_score(player_hand)
        print(f"Your Score: {player_score}")
        ace = check_ace(player_hand)
        print(f"Ace?: {ace}")
        if player_score == 21:
            print(f"BLACKJACK!!! Your score: {player_score}")
            wallet = db.add_money(wallet, bet * 2.5)
            print()
            
        
        #player choice
        while True:
            choice = input("Hit or stand? (hit/stand): ").lower()
            if choice == "hit":
                player_hand.append(deck.pop())
                player_score = add_player_score(player_hand)
                print(player_hand)
                print(f"Your Score: {player_score}")
                ace = check_ace(player_hand)
                print(f"Ace?: {ace}")
                if player_score > 21:
                    print(f"BUST! You Lose.")
                    print()
                    print(f"Remaining balance: ${wallet:.2f}")
                    print()
                    break
                elif player_score == 21:
                    print(f"BLACKJACK!!! Your score: {player_score}")
                    wallet = db.add_money(wallet, bet * 2.5)
                    print(f"Balance: ${wallet:.2f}")
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
            house_score = add_house_score(house_hand)
            print(f"House Score: {house_score}")

            #While house has a score less than 17 they must hit   
            while house_score < 17:
                print("House draws another card")
                time.sleep(2)
                house_hand.append(deck.pop())
                house_score = add_house_score(house_hand)
                print(house_hand)
                print(f"House Score: {house_score}")

            #final check of house outcome        
            if house_score > 21:
                print(f"BUST! House score: {house_score}")
                print()
                print("You Win!")
                wallet = db.add_money(wallet, bet * 2)
                print(f"Balance: ${wallet:.2f}")
            elif house_score == 21:
                print(f"BLACKJACK!!! House score: {house_score}")
                print()
                print("House Wins!")
                print()
                print(f"Remaining balance: ${wallet:.2f}")
            elif house_score > player_score:
                print("House wins!")
                print()
                print(f"Remaining balance: ${wallet:.2f}")
            elif house_score < player_score:
                print("You Win!")
                wallet = db.add_money(wallet, bet * 2)
                print(f"Balance: ${wallet:.2f}")
                print()
            else:
                print("PUSH")
                print()
                wallet = db.add_money(wallet, bet)
                print(f"Balance: ${wallet:.2f}")
                
                
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
