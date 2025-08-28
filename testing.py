#Find the missing letter

#Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

#You will always get a valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#Example:

#['a','b','c','d','f'] -> 'e'
#['O','Q','R','S'] -> 'P'

#(Use the English alphabet with 26 letters!)
import string

def find_missing_letter(letters_arr):
    counter = 0
    missing = ""
    alphabet = list(string.ascii_letters)

    #slicing attempt
    str_alphabet = "".join(alphabet)
    str_letters_arr = "".join(letters_arr)

    alph_sliced = str_alphabet[alphabet.index(str_letters_arr[0]):alphabet.index(str_letters_arr[-1]) + 1]
    alph_sliced_list = list(alph_sliced)

    for letter in alph_sliced_list:
        if letters_arr[counter] == letter:
            counter+=1
            continue
        else:
            missing += letter
    print(missing)


find_missing_letter(['O','Q','R','S'])



