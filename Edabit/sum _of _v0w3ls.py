#Edabit - Sum of v0w3ls 


def sum_of_vowels(string):
    vowels = {
        "A" : 4,
        "E" : 3,
        "I" : 1,
        "O" : 0,
        "U" : 0
    }
    result = 0
    for character in string.upper():
        if character in vowels:
            result += vowels[character]
    return result


print(sum_of_vowels("I love edabit!"))
