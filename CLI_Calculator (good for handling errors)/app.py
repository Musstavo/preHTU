def show_menu():
    print("1- Addition")
    print("2- Subtraction")
    print("3- Multiply")
    print("4- Division")
    print("5- Exit")

def addition():
    x = int(input("Choose the first number: "))
    y = int(input("Choose the second number: "))
    sum = f"{x} + {y} = {x+y}\n"
    l.append(sum)
    print(sum)

def subtraction():
    x = int(input("Choose the first number: "))
    y = int(input("Choose the second number: "))  
    sum = f"{x} - {y} = {x-y}\n"
    l.append(sum)
    print(sum)

def multiply():
    x = int(input("Choose the first number: "))
    y = int(input("Choose the second number: "))
    sum = f"{x} * {y} = {x*y}\n"  
    l.append(sum)
    print(sum)

def division():
    x = int(input("Choose the first number: "))
    y = int(input("Choose the second number: "))
    sum = f"{x} / {y} = {x/y}\n"
    l.append(sum)
    print(sum)

    

def main():
    while True:
        show_menu()
        try:
            choice = int(input("\nChoose what to do: "))
            if choice == 1:
                addition()
            if choice == 2:
                subtraction()
            if choice == 3:
                multiply()
            if choice == 4:
                division()
            if choice == 5:
                break    
        except ValueError:
            print("TYPE A NUMBER YOU STUPID FUCKING IDIOT!\n")
        except ZeroDivisionError:
            print("You can't divide by zero! dumbfuck.. \n")
    print("\n".join(l))        
l = []            
main()
