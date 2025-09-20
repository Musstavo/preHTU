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

    if len(height) < 3 and (height[0] == 0 or height[1] == 0):
        print(0)

    # (distance) * min(height[first], height[second])

    first_index = 0
    second_index = 1
    while first_index < len(height) - 1:
        if accumilater[first_index][1] > accumilater[second_index][1]:
            areas.append(
                abs(accumilater[first_index][0] - accumilater[second_index][0])
                * (accumilater[second_index][1])
            )
        else:
            areas.append(
                abs(accumilater[first_index][0] - accumilater[second_index][0])
                * (accumilater[first_index][1])
            )
        second_index += 1
        if second_index == len(height):
            first_index += 1
            second_index = 1
        if len(areas) == 2:
            if areas[0] > areas[1]:
                areas.pop(1)
            else:
                areas.pop(0)
    print(areas[0])


maxArena([8, 7, 2, 1])
