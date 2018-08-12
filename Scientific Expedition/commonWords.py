#!/usr/bin/python
# -*- Coding: utf-8 -*-


def checkio(first, second):
    a = []
    first = first.split(',')
    second = second.split(',')
    first.sort()
    second.sort()
#    print('first = ' + str(first))
#    print('second = ' + str(second))
    for i in first:
        for j in second:
            if i == j:
                a.append(i)
    a = ','.join(a)
#    print('a = ' + str(a))
    return a


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
