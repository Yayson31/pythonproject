

#Money system 

filename = "money.txt"

def load_wallet(filename = "money.txt"):
    try:
        with open(filename, "r") as file:
            return float(file.read())
    except FileNotFoundError:
        print("File not found... Creating new wallet")
        return 0.0
    except ValueError:
        return 0.0
    

def save_wallet(balance, filename = "money.txt"):
    with open(filename, "w") as file:
        file.write(str(balance))


def add_money(balance, amount):
    balance += amount
    save_wallet(amount)
    return balance

def bet_money(balance, bet):
    balance -= bet
    save_wallet(balance)
    return balance






if __name__ == "__main__":
    main()
