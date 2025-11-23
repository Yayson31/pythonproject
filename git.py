import random

def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

def create_deck(deck):
    for suit in ["C", "D", "H", "S"]:
        for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            deck.append(rank+suit)



def shuffle_deck(deck):
    random.shuffle(deck)


'''def play_game(deck):'''
    
    


def main():
    title()
    bank = 100.0
    while True:
        print(f"Money: {bank}")
        bet = float(input(f"Bet: "))
        print()
        
        deck = []
        create_deck(deck)
        shuffle_deck(deck)

        player_card1 = random.choice(deck)
        cpu_card1 = random.choice(deck)
        player_card2 = random.choice(deck)
        cpu_card2 = random.choice(deck)

        print(f"DEALER'S SHOW CARD:\n{cpu_card1}")
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
                break
                
        

        






        choice3 = input("Go again? (y/n): ")
        if choice3 == "n":
            print()
            print("Bye")
            break


if __name__ == "__main__":
    main()
