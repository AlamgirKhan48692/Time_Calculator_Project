def add_time(start, duration, start_day=None):
    # Days of the week for reference
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse start time
    time, meridian = start.split()
    start_hour, start_minute = map(int, time.split(":"))

    # Convert start time to 24-hour format
    if meridian == "PM":
        start_hour += 12 if start_hour != 12 else 0
    elif start_hour == 12:  # Midnight case
        start_hour = 0

    # Parse duration
    dur_hours, dur_minutes = map(int, duration.split(":"))

    # Add duration
    end_minute = start_minute + dur_minutes
    end_hour = start_hour + dur_hours + (end_minute // 60)
    end_minute %= 60

    # Calculate number of days later
    days_later = end_hour // 24
    end_hour %= 24

    # Convert back to 12-hour format
    if end_hour == 0:
        display_hour = 12
        meridian = "AM"
    elif end_hour < 12:
        display_hour = end_hour
        meridian = "AM"
    elif end_hour == 12:
        display_hour = 12
        meridian = "PM"
    else:
        display_hour = end_hour - 12
        meridian = "PM"

    # Format the new time
    new_time = f"{display_hour}:{end_minute:02d} {meridian}"

    # Add day of the week if provided
    if start_day:
        index = days.index(start_day.capitalize())
        new_day = days[(index + days_later) % 7]
        new_time += f", {new_day}"

    # Add day info
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


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

