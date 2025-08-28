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
    missing = ""
    alphabet = list(string.ascii_letters)

    #slicing attempt SUCCESS ( NEED TO FIND THE MISSING LETTER NOW )
    str_alphabet = "".join(alphabet)
    str_letters_arr = "".join(letters_arr)

    alph_sliced = str_alphabet[alphabet.index(str_letters_arr[0]):alphabet.index(str_letters_arr[-1]) + 1]
    print(alph_sliced)


    #for i,char in enumerate(alphabet):
    #    if alphabet[i] in letters_arr:
    #      continue
    #  if alphabet[i] != letters_arr[i]:


find_missing_letter(['O','Q','R','S'])



