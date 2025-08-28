import random
password = ['0','9','8','7','6','5','4','3','2','1','^','!','$','@','#','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number_of_passwords = int(input("Number of passwords: "))
password_length = int(input("\nPassword length: "))

for num in range(1,number_of_passwords+1):
    random.shuffle(password)
    print(f"\n{"".join(password[:password_length-1])}")




