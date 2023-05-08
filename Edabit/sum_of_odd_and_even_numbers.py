#Edabit - Sum of Odd and Even Numbers 


def sum_evens_and_odds(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    odds = [x for x in numbers if x % 2 != 0]
    return [sum(evens), sum(odds)]


print(sum_evens_and_odds([1, 2, 3, 4, 5, 6]))
