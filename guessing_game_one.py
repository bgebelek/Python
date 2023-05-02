#Practice Python - Exercise 9 - Guessing Game One 


import random


def guess_number():
    answer = random.randint(1, 9)
    guesses = 0
    while True:
        guess = input("Pick a number from 1 to 9 or type exit to stop playing: ")
        if guess == "exit":
            break
        else:
            guess = int(guess)
            if 1 <= guess <= 9:
                if guess < answer:
                    guesses += 1
                    print("Too low!")
                elif guess > answer:
                    guesses += 1
                    print("Too high!")
                else:
                    guesses += 1
                    print(f"Correct! Total Guesses: {guesses}")
                    answer = random.randint(1, 9)
                    guesses = 0


guess_number()
