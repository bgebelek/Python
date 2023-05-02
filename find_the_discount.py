#Edabit - Find the Discount


def discounted_price(price, discount):
    return f"${round(price * ((100 - discount) / 100), 2)}"


print(discounted_price(89, 20))
