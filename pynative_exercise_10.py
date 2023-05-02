#Pynative - Exercise 10


def evens_and_odds(list1, list2):
    odds, evens = [y for y in list1 if y % 2 != 0], [x for x in list2 if x % 2 == 0]
    odds.extend(evens)
    return sorted(odds)


print(evens_and_odds([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]))
