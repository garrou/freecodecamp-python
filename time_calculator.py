DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
AM_PM = ["AM", "PM"]

def add_time(start, duration, day=None):

    [start_hours, start_minutes, meridian] = map(lambda x: int(x) if x.isdigit() else x, start.replace(":", " ").split(" "))
    [duration_hours, duration_minutes] = map(lambda x: int(x), duration.split(":"))

    hours = start_hours + duration_hours
    minutes = start_minutes + duration_minutes
    added_day = int(hours / 24)
    days_later = ""

    if minutes > 59:
        hours += 1
        minutes %= 60

    if meridian == AM_PM[1] and duration_hours % 12 + hours >= 12:
        added_day += 1

    meridian = AM_PM[(AM_PM.index(meridian) + int(hours / 12)) % len(AM_PM)]
    hours = 12 if hours % 12 == 0 else hours % 12
    minutes = minutes if minutes > 9 else "0" + str(minutes)

    if added_day == 1:
        days_later = "(next day)"
    elif added_day > 1:
        days_later = f"({added_day} days later)"

    if day == None:
        time = f"{hours}:{minutes} {meridian} {days_later}"
    else:
        dow = DAYS[(DAYS.index(day.title()) + added_day) % len(DAYS)]
        time = f"{hours}:{minutes} {meridian}, {dow} {days_later}"

    return time.strip()

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

print(add_time("11:55 AM", "3:12"))
# Returns: 3:07 PM

print(add_time("8:16 PM", "466:02")) 
# Returns: 6:18 AM (20 days later)

print(add_time("11:59 PM", "24:05", "Wednesday"))
# Returns: 12:04 AM, Friday (2 days later)

print(add_time("11:59 PM", "24:05"))
# Returns: 12:04 AM, (2 days later)

print(add_time("2:59 AM", "24:00"))
# Returns: 2:59 AM (next day)