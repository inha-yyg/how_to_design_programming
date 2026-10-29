GOAL = 60

def remaining(minutes):
    if minutes < GOAL:
        return GOAL - minutes
    else:
        return 0

print(remaining(20))
print(remaining(60))
print(remaining(80))                                             