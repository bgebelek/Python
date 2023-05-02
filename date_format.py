#Edabit - Date Format 


def date_formatter(date):
    return "".join(date.split("/")[-1::-1])


print(date_formatter("01/15/2019"))
