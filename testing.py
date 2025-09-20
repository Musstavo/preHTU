# You are given an integer array height of length n.
#  There are n vertical lines drawn
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
#  such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


def maxArena(height):
    accumilater = []
    areas = []
    for x, y in enumerate(height, start=1):
        couple = [x, y]
        accumilater.append(couple)
    print(accumilater)

    first_index = 0
    second_index = 1
    # while len(areas) != pow(len(accumilater), 2):
    for c in range(pow(len(accumilater), 2)):
        if accumilater[first_index][1] > accumilater[second_index][1]:
            print(
                abs(accumilater[first_index][0] - accumilater[second_index][0])
                * (accumilater[first_index][1] - accumilater[second_index][1])
            )
        else:
            print(
                abs(accumilater[first_index][0] - accumilater[second_index][0])
                * (accumilater[first_index][1])
            )
    first_index += 1
    second_index += 1


maxArena([1, 8, 6, 2, 5, 4, 8, 3, 7])
