#Edabit - Curzon Numbers


def curzon(num):
    return ((1 + 2**num) % (1 + (2 * num))) == 0


print(curzon(115))
