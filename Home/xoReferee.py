from typing import List

def checkio(game_result: List[str]) -> str:
    winner = "D"
    list0 = game_result[0]
    list1 = game_result[1]
    list2 = game_result[2]
    list3 = list0[0] + list1[0] + list2[0]
    list4 = list0[1] + list1[1] + list2[1]
    list5 = list0[2] + list1[2] + list2[2]
    list6 = list0[0] + list1[1] + list2[2]
    list7 = list0[2] + list1[1] + list2[0]
    list = [list0, list1, list2, list3, list4, list5, list6, list7]
#    print(list)
    for i in list:
        if i == "XXX":
            winner = "X"
        elif i == "OOO":
            winner = "O"
#    print("Draw")
    return winner


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")