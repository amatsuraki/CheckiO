def checkio(number: int) -> str:
    if number % 15 == 0:
        number = "Fizz Buzz"
    elif number % 5 == 0:
        number = "Buzz"
    elif number % 3 == 0:
        number = "Fizz"
    else:
        pass

    return str(number)


test = [15, 6, 5, 7]

for i in range(len(test)):
    item = test[i]
    print(checkio(item))
