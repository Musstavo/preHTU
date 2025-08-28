from random_words import words
import random
import re

random_word = random.choice(words).upper()
word_as_dashes = re.sub("[A-Z]","_",random_word)
print(word_as_dashes)
result = list(word_as_dashes)
used = []
lives = 8

while True:
    guess = input("Enter a letter: ").upper()
    matches = re.finditer(guess, random_word)
       
    for match in matches:
        if guess != "" and len(guess) == 1 and guess.isalpha() and guess not in used:
            result[match.start()] = guess
            used.append(guess)
        else:
            continue


    print("".join(result))
    if guess not in random_word and guess not in used and len(guess) == 1:
        used.append(guess)
        lives -= 1
    else:
        continue
    
    if not guess.isalpha():
        print("NOT A NUMBER YOUR MORON!")
        lives += 1
        continue

    print(lives)
    if lives == 0:
        print("Game over..")
        break

    

    if "".join(result) == random_word:
        print(f"You did it! the word was: {"".join(result)}")
        break



