#Edabit - Luke, I Am Your ...


def relation_to_luke(person):
    family = {"Darth Vader":"father", "Leia":"sister", "Han":"brother in law", "R2D2":"droid"}
    return f"Luke, I am your {family[person]}."


print(relation_to_luke("Han"))
