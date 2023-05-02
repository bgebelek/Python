#Mosh Hamedani - Exercise 3


def demerit_points(speed):
    if speed <= 70:
        return "Ok"
    else:
        points = -1
        for x in range (70, speed + 1, 5):
            if points == 12:
                return "License Suspended"
            points += 1
        return f"Points: {points}"


print(demerit_points(80))
