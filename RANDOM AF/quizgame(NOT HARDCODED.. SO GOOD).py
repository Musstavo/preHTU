questions = ["Question 1: What is the output of print(2 + 2)",
             "Question 2: Which data type is used to store text?",
             "Question 3: What keyword is used to define a function in Python?"]

options = [['a 3','b 4','c 5'],
           ['a int','b float', 'c str'],
           ['a def', 'b func', 'c define']]

answers = ['b', 'c', 'a']
user_answers = []

n = 0 

print("Welcome to the quiz game!\n")

for option in options:
    index = options.index(option)
    print(f"\n{questions[index]}")    
    for ans in option:
        print(ans)
    choice = input("Your anwer: ")
    user_answers.append(choice.lower())
    if user_answers[n] == answers[n]: 
        print("Correct!")
        n+=1  
    else:
        print("Wrong!")
        n-=1
        if n < 0:
            n=0
        

print("\nQuiz Complete!")
print(f"You got {n} out of {len(questions)} questions right.")
print(f"Your score: {int(n/len(questions)*100)}%")

        