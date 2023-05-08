#Mosh Hamedani - Exercise 4


def show_numbers(limit):
    for x in range(0, limit + 1):
        if x % 2 == 0:
            print(f"{x} EVEN")
        else:
            print(f"{x} ODD")


show_numbers(8)
