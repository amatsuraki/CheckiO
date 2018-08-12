class Warrior:
    attack = 5
    health = 50
    is_alive = True


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    print('fight')
    flag = True
    while unit_1.health > 0 and unit_2.health > 0:
        if flag is True:
            unit_2.health -= unit_1.attack
            flag = False
        else:
            unit_1.health -= unit_2.attack
            flag = True
    if unit_1.health > 0:
        print('unit1 win')
        unit_2.is_alive = False
        return True
    elif unit_2.health > 0:
        print('unit2 win')
        unit_1.is_alive = False
        return False
    else:
        print('error')


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")