#Practice Python - Exercise 13 - Fibonacci


def fibonnaci():
    num = int(input("Number: "))
    if num < 0:
        return "Error"
    elif num == 0:
        return []
    else:
        result = [0, 1]
        for _ in range(num - 1):
            result.append(result[-2] + result[-1])
        return result[1:]


print(fibonnaci())
