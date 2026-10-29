MINUTES_PER_HOUR = 60

def minutes_to_hours(minutes):
    return minutes/MINUTES_PER_HOUR

def remaining_time(goal, studied):
    if goal > studied:
        return goal - studied
    else:
        return 0

def remaining_hours(goal, studied):
    if goal > studied:
        return minutes_to_hours(goal - studied)
    else:
        return 0

print(minutes_to_hours(30))
print(remaining_time(60, 20))
print(remaining_hours(90, 30))
print(remaining_hours(60, 80))