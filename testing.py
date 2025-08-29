#Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
# You don't need to validate the form of the Roman numeral.

#Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
# starting with the leftmost digit and skipping any 0s.
# So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
# The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
#Example:

#"MM"      -> 2000
#"MDCLXVI" -> 1666
#"M"       -> 1000
#"CD"      ->  400
#"XC"      ->   90
#"XL"      ->   40
#"I"       ->    1

#Help:
#Symbol    Value
#I          1
#V          5
#X          10
#L          50
#C          100
#D          500
#M          1,000


# ACTUALLY DIFFICULT :'(
# so if we say "DC" it will == 600 because D > C, but "CD" will == 400 because C < D (WEIRD AF)
# step-by-step and it will be solved.. hopefully

def sol(roman_numeral):
    result = 0
    roman_dict = {"I":1,
                  "V":5,
                  "X":10,
                  "L":50,
                  "C":100,
                  "D":500,
                  "M":1000}

 # FAILED TRY due to hard coding ( LOOPING THROUGH THE DICT ) NO POINT IT SEEMS.
 #   for i,k in enumerate(roman_dict):
 #       if i < len(roman_numeral)-1:

 #           if roman_dict[roman_numeral[i+1]] < roman_dict[roman_numeral[i]]:
 #              result += roman_dict[roman_numeral[i+1]] + roman_dict[roman_numeral[i]]
 #           if roman_dict[roman_numeral[i+1]] > roman_dict[roman_numeral[i]]:
 #              result += roman_dict[roman_numeral[i+1]] - roman_dict[roman_numeral[i]]

 #   if len(roman_numeral) == 1:
 #        result += roman_dict[roman_numeral]
 #   print(result)



# second try, ITERATE THE ROMAN_NUMERAL NOT THE DICT (so far so good, now the exceptions --> X L C D
    for i,letter in enumerate(roman_numeral):
        key = roman_numeral[i]
        result+=roman_dict[key]
        if roman_dict[key]<:

    print(result)




    #okay the plan for tmr is as such, we'll do a loop from the maximum value to the least
    # (or opposite but it's gonna be a pain in the ass) and then check if one is larger than the other (D and C situation)
    # so basically no need for a billion if statements if you know what you're doing

sol("MM")