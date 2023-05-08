#Practice Python - Exercise 15 - Reverse Word Order 


def reverse_sentence(sentence):
    return " ".join(sentence.split(" ")[-1::-1])


print(reverse_sentence("My name is Michele"))
