# Edabit - Two Distinct Elements


def return_unique(numbers):
    result = []
    for number in numbers:
        if numbers.count(number) == 1:
            result.append(number)
    return result


print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
