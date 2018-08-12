def correct_sentence(str):
    text = str[0].upper() + str[1:]
    if text.endswith("."):
        pass
    else:
        text = text + "."


str1 = "greetings, friends"
str2 = "Greetings, friends"
str3 = "Greetings, friends."
str4 = "hello New York"

correct_sentence(str1)
correct_sentence(str2)
correct_sentence(str3)
correct_sentence(str4)
