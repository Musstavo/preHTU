#You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones

# -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block,

# so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
# and will, of course, return you to your starting point. Return false otherwise.

#Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).
# It will never give you an empty array (that's not a walk, that's standing still!).


# A BIT DIFFICULT ( very in fact.. the returning to the og position is a pain )

# BRAIN STORMING
# wtf ???? the len(array) must be == 10 and returning to my og location just like below
# if it's ['s','s','n','n','n','s','s','s,'n','n'] i think it should return True
# OKAY WAIT, if we compare 's' and 'n' alone, and 'w' and 'e' alone.. basically creating a counter
# that if walk[0] == 'n' and walk[1] == 's' then we add one to the counter, but if we encounter another 'n' we subtract one
# same thing with 'e' and 'w' i believe..

#first issue: the first index... hard code it?! surely not.


#ATTEMPT ONE
def is_valid_walking(walk):
    counter = 0
    for i,direction in enumerate(walk):
        if len(walk[direction]) == 10:
            if walk[i] != walk[i+1]:
                counter += 1


        else:
            print(False)

is_valid_walking(['s','s','n','n','n','s','s','s','n','n'])




















