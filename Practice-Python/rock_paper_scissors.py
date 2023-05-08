#Practice Python - Exercise 8 - Rock Paper Scissors


def rock_paper_scissors():
    while True:
        choice1 = str(input("Player 1, choose: rock, paper, or scissors. "))
        choice2 = str(input("Player 2, choose: rock, paper, or scissors. "))
        if (choice1 == "rock" or choice1 == "paper" or choice1 == "scissors") and (choice2 == "rock" or choice2 == "paper" or choice2 == "scissors"):
            if choice1 == "rock":
                if choice2 == "rock":
                    return "Draw"
                if choice2 == "paper":
                    return "Player 2 won!"
                if choice2 == "scissors":
                    return "Player 1 won!"
            elif choice1 == "paper":
                if choice2 == "rock":
                    return "Player 1 won!"
                if choice2 == "paper":
                    return "Draw"
                if choice2 == "scissors":
                    return "Player 2 won!"
            else:
                if choice2 == "rock":
                    return "Player 2 won!"
                if choice2 == "paper":
                    return "Player 1 won!"
                if choice2 == "scissors":
                    return "Draw"


print(rock_paper_scissors())
