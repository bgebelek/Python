#Edabit - Length of Number 


def length(num):
    num = str(num)
    return int(num.rindex(num[-1])) + 1


print(length(1234))
