#Pynative - Exercise 11


def reverse(num):
    return " ".join([x for x in str(num)][-1::-1])


print(reverse(7536))
