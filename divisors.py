#Practice Python - Exercise 4 - Divisors


def divisors(num):
    return [x for x in range(1, num + 1) if num % x == 0]


print(divisors(int(input("Number: "))))
