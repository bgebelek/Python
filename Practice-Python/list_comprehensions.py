#Practice Python - Exercise 7 - List Comprehensions


def even_numbers(list):
    return [x for x in list if x % 2 == 0]


print(even_numbers([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))
