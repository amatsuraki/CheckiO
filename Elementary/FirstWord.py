# -*- coding: utf-8 -*-

"""returns the first word in a given text."""


def first_word(text: str) -> str:
    print(text)
    text = text.replace(",", " ").replace(".", " ")
    text = text.strip().split()
    return text[0]


test = [
        "Hello world", " a word ", "don't touch it", "greetings, friends",
        "... and so on ...", "hi", "Hello.World"
        ]
"""
test1 = "Hello world"
test2 = " a word "
test3 = "don't touch it"
test4 = "greetings, friends"
test5 = "... and so on ..."
test6 = "hi"
test7 = "Hello.World"
"""

for i in range(len(test)):
    test_item = test[i]
    print(first_word(test_item))
