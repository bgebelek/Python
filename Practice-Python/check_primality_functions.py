#Practice Python - Exercise 11 - Check Primality Functions 


def prime_number(num):
    if num > 1:
        if num == 2 or num == 3:
            return True
        return not (num % 2 == 0 or num % 3 == 0)
    return "Prime number must be greater than 1"


print(prime_number(9))
