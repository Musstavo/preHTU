import random

symbols = ['🍒','🍉','🍋','🔔','⭐']
results = []

def menu():
    print("**********************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("**********************")
    

      
def main():
    balance = 100
    menu() 
    while True:
        print(f"Current balance: ${balance}")
        bet_amount = input("Place your bet amount: ")
        if not bet_amount.isdigit():
            print("Enter a valid number\n")
            continue   
        print("Spinning...\n\n")
        print("***********")
        for num in range(3):
            pick = random.choice(symbols)
            results.append(pick)
        for symbol in results:
            print(f"{symbol}", end=" ")
        if results.count(symbol) == 3:
            balance *= 2
            print(f"\nNice, your balance has doubled and became: ${balance}!")
        if int(bet_amount) > balance:
            print("Insufficient funds\n")
            continue
        elif int(bet_amount) <= balance:
            balance -= int(bet_amount)
        elif balance == 0:
            print("YOU LOST!")
            break            
        else:
            print("\nSorry you lost this round")
        again = input("\nDo you want to spin again? (Y/N): ")

        if again.lower() == 'y':
            results.clear()
            continue
        if again.lower() == 'n':
            break
        print("\n***********")  
if __name__ == '__main__':
    main()