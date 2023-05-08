#Practice Python - Exercise 1 - Character-Input 


def year_determiner(name, age):
    return f"{name} will turn 100 at {2023 + (100 - age)}"

def message_repeater(message):
    while True:
        decision = str(input("Do you want your message repeated? (Y/N): "))
        if decision == "Y" or decision == "y":
            num = int(input("Number: "))
            return (f"{message}\n") * num
        elif decision == "N" or decision == "n":
            return message
            
            
print(message_repeater(year_determiner(str(input("Name: ")), int(input("Age: ")))))
