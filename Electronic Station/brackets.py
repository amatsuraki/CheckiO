#!/usr/bin/python
# -*- Coding: utf-8 -*-

def checkio(expression):
    print('expression = {}'.format(expression))
    list = []
    brackets = {"(":")", "[":"]", "{":"}"}
    for i in expression:
        if i in brackets.keys():
            list.append(i)
#            print('{} append'.format(i))
        elif i in brackets.values():
#            print('{} in values'.format(i))
            if not list:
                return False
            else:
                for k, v in brackets.items():
#                    print('i = {}'.format(i))
#                    print('v = {}'.format(v))
                    if i == v:
                    """
                        print('{} = {}'.format(i, v))
                        print('k = {}'.format(k))
                        print('list = {}'.format(list))
                        print('list[-1] = {}'.format(list[-1]))
                        """
                        if k == list[-1]:
                            del list[-1]
#                            print('{} deleted'.format(k))
                        else:
#                            print('false')
                            return False
#    print('list = {}'.format(list))
    if not list:
#        print('{} is true'.format(expression))
        return True
    else:
#        print('{} is false'.format(expression))
        return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("(((([[[{{{3}}}]]]]))))") == False
    assert checkio("({3}])") == False
