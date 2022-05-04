def add_time(start, duration, *day):

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Start time formatting
    start = start.split()
    start_hour = int(start[0].split(':')[0])
    start_minute = int(start[0].split(':')[1])
    am_pm = start[1].upper()


    # Duration time formatting
    duration = duration.split()
    duration_hour = int(duration[0].split(':')[0])
    duration_minute = int(duration[0].split(':')[1])

    if am_pm == "PM":
        start_hour += 12

    # Resolution variables
    res_hour = start_hour + duration_hour
    res_minute = start_minute + duration_minute
    res_day_quote = ""
    res_am_pm = ""
    res_week_day = ""
    res_day = 0


    if res_minute >= 60:
        res_hour += 1
        res_minute -= 60

    if res_hour > 24:
        res_day = res_hour // 24
        res_hour = res_hour % 24
        if res_day == 1:
            res_day_quote = " (next day)"
        elif res_day > 1:
            res_day_quote = f" ({res_day} days later)"

    if res_hour == 0:
        res_hour += 12
        res_am_pm = "AM"
    elif res_hour >= 12:
        res_am_pm = "PM"
        if res_hour > 12:
            res_hour = res_hour % 12
    else:
        res_am_pm = "AM"

    new_time = f"{res_hour}:{res_minute:02d} {res_am_pm}{res_day_quote}"

    if day:
        day = day[0].capitalize()
        day_index = days_of_week.index(day)
        if res_day == 0:
            new_time = f"{res_hour}:{res_minute:02d} {res_am_pm}, {day}{res_day_quote}"
        elif res_day == 1:
            day_index += 1
            res_week_day = days_of_week[day_index]
            new_time = f"{res_hour}:{res_minute:02d} {res_am_pm}, {res_week_day}{res_day_quote}"
        elif res_day > 1:
            for i in range(res_day):
                day_index = (day_index + 1) % 7
                day = days_of_week[day_index]
                res_week_day = day

            new_time = f"{res_hour}:{res_minute:02d} {res_am_pm}, {res_week_day}{res_day_quote}"

    return new_time


print(add_time("8:16 PM", "466:02", "tuesday"))








