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
    roman_dict = {"I":1,
                  "V":5,
                  "X":10,
                  "L":50,
                  "C":100,
                  "D":500,
                  "M":1000}

    # Accessing a numeral's value form the dict
    #if roman_numeral in roman_dict:
    #    print(roman_dict[roman_numeral])

    #if roman_numeral[0] == roman_numeral[1]:
    #    print(roman_dict[roman_numeral[0]]*2)

    #okay the plan for tmr is as such, we'll do a loop from the maximum value to the least
    # (or opposite but it's gonna be a pain in the ass) and then check if one is larger than the other (D and C situation)
    # so basiaclly no need for a billion if statemnts if you know what you're doing


sol("MM")