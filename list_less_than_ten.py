#Practice Python - Exercise 3 - List Less Than Ten 


def generate_list(list, num):
    return [x for x in list if x < num]


print(generate_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], int(input("Number: "))))
