def to_encrypt(text, delta):
#    print("text = " + text)
    out = ""
    if delta < 0:
        delta += 26
#    print("delta is " + str(delta))
    for i in text:
#        print(i + " = " + str(ord('i')))
        x = ord(i) + delta
        if i == " ":
            out += " "
#            print(" ")
        elif x <= ord('z'):
            out += chr(x)
#            print("+ " + str(x))
        elif ord('z') < x:
            out += chr((ord(i) - ord('a') + delta) % 26 + ord('a'))
#    print("out = " + out)
    return out


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
