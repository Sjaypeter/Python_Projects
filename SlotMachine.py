import random

def spin_row():
    symbols = ['🍒', '🍌', '🍉', '🔔', '⭐']
    
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
        
    return results

def print_row(row):
    print("|" .join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        
        elif row[0] == "🍌":
            return bet * 4
        
        elif row[0] == "🍉":
            return bet * 5
        
        elif row[0] == "🔔":
            return bet * 10
        
        elif row[0] == "⭐":
            return bet * 20
        
    return 0


def main():
    Balance = 100
    
    print("---------------------------")
    print("Welcome to Slot Machine")
    print("Symbols: 🍒 🍌 🍉 🔔 ⭐")
    print("---------------------------")
    
    while Balance > 0:
        print(f"Current balance is {Balance}")
        
        bet = int(input("Place amount you want to bet: "))
        
        if bet > Balance:
            print("Insufficient funds")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        Balance -= bet
        
        row = spin_row()
        print("Spinning....\n")
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
            
        else:
            print("Sorry you lost this round")
            
        Balance += payout
        
        play_again = input("Do you want to spin again(Y/N) ").upper()
        if play_again != "Y":
            break
    
    print("---------------------------")    
    print(f"Game over! Your final balance is ${Balance}")
    print("---------------------------")    
if __name__ == "__main__":
    main()