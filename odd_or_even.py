#Practice Python - Exercise 2 - Odd or Even 


def odd_or_even(num):
    if num % 4 == 0:
        return "Multiple of 4"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(odd_or_even(int(input("Number: "))))
