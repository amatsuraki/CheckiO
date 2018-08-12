#!/usr/bin/python
# -*- Coding: utf-8 -*-

def is_stressful(subj):
    stress = False
    keys = ['help', 'asap', 'urgent']
    text, j = '', ''
    if subj.isupper():
        stress = True
#        print('{} is all upper'.format(subj))
    elif subj.endswith('!!!'):
        stress = True
#        print('{} ends with !!!'.format(subj))
    else:
        subj = subj.lower()
        for i in subj:
            if i.isalpha() and i != j:
                text += i
            j = i
#        print('text is {}'.format(text))
        for k in keys:
            if text.find(k) != -1:
                stress = True
#                print('{} has key word'.format(text))
#    if stress is False:
#        print('{} is false'.format(subj))
    return stress


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("UUUURGGGEEEEENT here") == True, "Third"
    print('Done! Go Check it!')