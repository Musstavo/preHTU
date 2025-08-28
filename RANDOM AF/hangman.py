import random
from random_words import words

random_word = random.choice(words).upper()
lives = 6
letters_guessed = ""
amount_of_dashes = "-" * len(random_word)

while True:

    guess = input("\n\nGuess a letter: ").upper()
    letters_guessed += guess + ""

    if guess == " ":
        letters_guessed = letters_guessed.replace(" ","")
        print("Input cannot be blank, Please try again.")

    if guess not in random_word:
        print(f"\nCurrent word: {amount_of_dashes}")
        if letters_guessed.count(guess) == 1:
            lives -= 1

    if lives == 0:
        print(f"\nGame over.. the word was {random_word}")
        break
        
    if letters_guessed.count(guess) > 1 and guess not in random_word:
        last_index = letters_guessed.rfind(guess)
        letters_guessed = letters_guessed[:last_index] + "" + letters_guessed[last_index+1:]

    print(f"\nYou have {lives} lives left and you have used these letters: {letters_guessed}\n")

    if guess in random_word:
        for char in random_word:
            index_of_letter = random_word.find(guess)
            amount_of_dashes = amount_of_dashes[:index_of_letter] + guess + amount_of_dashes[index_of_letter+1:]
        print(f"Current word: {amount_of_dashes}")
        
    elif amount_of_dashes == random_word:
        print(f"\nCongratz! you guessd the word {random_word}")
        break