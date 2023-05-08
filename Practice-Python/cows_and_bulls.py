#Practice Python - Exercise 18 - Cows And Bulls 


import random


def cows_and_bulls():
    answer = str(random.randint(0000, 9999))
    print(answer)
    cows, bulls, guesses = 0, 0, 0
    temp = []
    while True:
        guess = input("Guess (4 digits only): ")
        if len(guess) == 4 and guess.isnumeric():
            for index in range(len(guess)):
                if guess[index] in answer:
                    if guess.index(guess[index]) == answer.index(guess[index]):
                        cows += 1
                    else:
                        if temp.count(guess[index]) != answer.count(guess[index]):
                            temp.append(guess[index])
                            bulls += 1
            guesses += 1
            if cows == 4:
                print(f"Cows: {cows}, Bulls: {bulls}, Guesses: {guesses}")
                break
            else:
                print(f"Cows: {cows}, Bulls: {bulls}, Guesses: {guesses}")
                cows, bulls = 0, 0
                temp = []


cows_and_bulls()
