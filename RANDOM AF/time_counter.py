import time
seconds = int(input("Enter the amount of seconds you want: "))


while seconds:

    minutes, seconds_left = divmod(seconds, 60)
    timer = f"{minutes:02d}:{seconds_left:02d}"
    time.sleep(1)
    seconds -= 1
    print(timer, end="\r")

print("Let's go!!!")