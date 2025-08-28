balance = 0

def menu():
    print("************************")
    print("    Banking Program")
    print("************************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("************************")


def show_balance(balance):
    return balance

def deposit(balance):
    deposit_amount = int(input("Enter the amount you want to deposit: "))
    if deposit_amount < 0:
        print("There isn't such thing as negative money, moron.")
        return balance
    else:
        balance += deposit_amount
        return balance

def withdraw(balance):
    withdraw_amount = int(input("Enter the amount you want to withdraw: "))
    if withdraw_amount <= balance: 
        balance -= withdraw_amount
        return balance
    elif withdraw_amount > balance or balance == 0:
        print(f"Your balance doesn't have enough money to withdraw {withdraw_amount}")
        return balance
    elif withdraw_amount < 0:
        print("There isn't such thing as negative money, moron.")
        return balance
        
while True:
    menu()
    try:
        user_choice = int(input("Enter your choice (1-4): "))
        if user_choice not in [1, 2, 3, 4]:
            print("Please enter a valid option between 1 and 4.\n")
            continue
        if user_choice == 4:
            print(f"Your account balance is: {balance}\n\n")
            break
        if user_choice == 1:
            balance = show_balance(balance)
            print(f"Your account balance is: {balance}\n\n")
        if user_choice == 2:
            balance = deposit(balance)
            print(f"Your account balance is: {balance}\n\n")
        if user_choice == 3:
            balance = withdraw(balance)
            print(f"Your account balance is: {balance}\n\n")
    except ValueError:
        print("Please enter a number.\n")