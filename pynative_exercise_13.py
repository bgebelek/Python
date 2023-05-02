#Pynative - Exercise 13


def multiplication_table(list):
    for x in list:
        for y in range(1, 11, 1):
            print(x * y, end = " ")
        print()


multiplication_table([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
