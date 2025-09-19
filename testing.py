# Your task is to sort a given string.
# Each word in the string will contain a single number.
# This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->"Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""


def order(sentence):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    empty = []
    new_empty = []
    new_index = 0
    for f, i in enumerate(sentence):
        if i == " ":
            empty.append(sentence[new_index:f])
            new_index = f
    empty.append(sentence[f - 1 :])
    new_empty = empty

    letter_index = 0
    for word in empty:
        if word[letter_index] in numbers:
            new_empty[word[letter_index] - 1] = word
            letter_index = 0
        else:
            letter_index += 1
    print(new_empty)


order("is2 Thi1s T4est 3a")
