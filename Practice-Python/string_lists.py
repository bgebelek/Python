#Practice Python - Exercise 6 - String Lists 


def string_palindrome(str):
    return str[:] == str[-1::-1]


print(string_palindrome("mom"))
