#Pynative - Exercise 12


def income_tax(salary):
    result = salary - 10000
    if result < 10000:
        return "Income Tax: $0.00"
    else:
        return f"Income Tax: ${(10000 * 0.10) + ((result - 10000) * 0.20)}"


print(income_tax(float(45000)))
