#Mosh Hamedani - Exercise 2


def fizz_buzz(num):
    result = []
    for x in range(1, num + 1):
        if x % 3 == 0 and x % 5 == 0:
            result.append("FizzBuzz")
        elif x % 3 == 0:
            result.append("Fizz")
        elif x % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(x))
    return result


print(fizz_buzz(15))
