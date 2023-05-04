#HackerEarth - Divisibility


def formed_number_divisible_by_10(numbers):
    for number in numbers:
        if str(number)[-1] != 0:
            return "No"
    return "Yes"


print(formed_number_divisible_by_10([85, 25, 65, 21, 84]))
