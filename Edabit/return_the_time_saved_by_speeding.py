#Edabit - Return the Time Saved by Speeding


def time_saved(speed_limit, average_speed, average_speed_distance):
    return round(((average_speed_distance * 60) / speed_limit) - ((average_speed_distance * 60) / average_speed), 1)


print(time_saved(80, 100, 10))
