def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    pre = ""        # previous character
    count = 1
    max = 0
    for i in line:
        print(i)
        if i == pre:
            count += 1
        else:
            count = 1
        if max < count:
            max = count
#            print("max = " + str(max))
        pre = i
#    print("final max = " + str(max))
    return max


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
