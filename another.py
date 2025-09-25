def histogram(values, bin_width):
    new = []
    test = []
    left = 0
    right = bin_width
    i = 0
    while i < len(values):
        for value in values:
            for e in range(left, right):
                if value == e:
                    test.append(values.count(value))
                    new.append(sum(test))
                    test.clear()

            i += bin_width
        left += bin_width
        right += bin_width
    print(new)


histogram([1, 1, 0, 1, 3, 2, 6], 2)
