def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if array:
        sum = 0
        for i in range(len(array)):
            last = array[i]
            if i % 2 == 0 or i == 0:
                sum += array[i]
            else:
                pass
        return sum * last
    else:
        return 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")