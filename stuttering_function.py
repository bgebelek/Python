#Edabit - Stuttering Function


def stutter(word):
    sentence = ""
    for x in range(0, 3):
        if x < 2:
            sentence += f"{word[0:2]}... "
        else:
            sentence += f"{word}?"
    return sentence


print(stutter("outstanding"))
