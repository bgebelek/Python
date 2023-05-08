#Edabit - Disarium Number


def is_disarium(number):
    result = 0
    for index, digit in enumerate(str(number)):
        result += int(digit) ** (index + 1)
    return result == number


print(is_disarium(8))
