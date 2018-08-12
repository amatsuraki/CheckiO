def checkio(text: str) -> str:

    a = list(text.lower())      # text
    b = []                      #
    dic = {}
    dic2 ={}

    for i in a:
        if not i.isalpha():
            pass
        elif i in b:
            pass
        else:
            b.append(i)
#            print(i + " append")
    for j in b:
        count = a.count(j)
        dic.update({j:count})
    for k, v in dic.items():
        if v == max(dic.values()):
            dic2.update({k:v})
        else:
            pass
    return  min(dic2.keys())


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
