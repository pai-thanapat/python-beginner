# 38. Match Case Statement


def day_of_week(day):
    match day:
        case 1:
            return "It's Monday."
        case 2:
            return "It's Tuesday."
        case 3:
            return "It's Wednesday."
        case 4:
            return "It's Thursday."
        case 5:
            return "It's Friday."
        case 6:
            return "It's Saturday."
        case 7:
            return "It's Sunday."
        case _:
            return "Invalid day."


def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case _:
            return False


day = day_of_week(3)
is_weekend_result = is_weekend("Saturday")

print(f"Day '3' of the week: {day}")
print(f"Is 'Saturday' the weekend? {is_weekend_result}")
