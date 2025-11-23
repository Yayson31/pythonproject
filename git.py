import random

def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

def create_deck(deck):
    for suit in ["C", "D", "H", "S"]:
        for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            deck.append(rank+suit)



def shuffle_deck(deck):
    random.shuffle(deck)


'''def play_deck():'''


    


def main():
    title()
    bank = 100.0
    while True:
        print(f"Money: {bank}")
        bet = float(input(f"Bet: "))
        
        deck = []
        create_deck(deck)
        shuffle_deck(deck)
        print(*deck, sep="\n")
        







        choice = input("Go again? (y/n): ")
        if choice == "n":
            print()
            print("Bye")
            break


if __name__ == "__main__":
    main()
