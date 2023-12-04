def parse_in_time(start_time):
    time, part_of_day = start_time.split()
    start_hour, start_minute = time.split(':')
    if part_of_day == 'PM':
        start_hour = int(start_hour) + 12
    return int(start_hour), int(start_minute)


def parse_duration(duration):
    duration_hour, duration_minutes = duration.split(':')
    return int(duration_hour), int(duration_minutes)


def days():
    return ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday')


def weekday(start_day):
    start_day = start_day.capitalize()
    tmp_start_day_index = days().index(start_day)
    return tmp_start_day_index


def calculate_hours(input_hour, input_minutes, duration_hours,
                    duration_minutes):
    tmp_hours = (input_minutes + duration_minutes) // 60
    output_minutes = (input_minutes + duration_minutes) % 60
    tmp_days = (input_hour + duration_hours + tmp_hours) // 24
    output_hours = (input_hour + duration_hours + tmp_hours) % 24
    return tmp_days, output_hours, output_minutes


def calculate_days(day_of_week, tmp_day, start_day):
    list_days = days()
    if tmp_day == 0 and start_day == '':
        return ('')
    elif tmp_day == 0 and start_day != '':
        return f', {start_day.capitalize()}'
    elif tmp_day == 1 and start_day == '':
        return ' (next day)'
    elif tmp_day > 1 and start_day == '':
        return f' ({tmp_day} days later)'
    else:
        finally_day = (tmp_day + day_of_week) % 7

        return f', {list_days[finally_day]} ({tmp_day} days later)'


def returning_hours(output_hours, output_minutes):
    part_of_day = 'PM' if output_hours >= 12 else 'AM'
    hour = output_hours % 12
    if hour == 0:
        hour = 12
    if output_minutes < 10:
        output_minutes = f'0{output_minutes}'
    return f'{hour}:{output_minutes} {part_of_day}'


def add_time(start_time, duration, start_day=''):
    day_of_week = 10
    start_hour, start_minute = parse_in_time(start_time)
    duration_hour, duration_minutes = parse_duration(duration)
    if start_day != '':
        day_of_week = weekday(start_day)
    tmp_days, output_hours, output_minutes = calculate_hours(
        start_hour, start_minute, duration_hour, duration_minutes)
    calculated_days = calculate_days(day_of_week, tmp_days, start_day)
    calculated_hours = returning_hours(output_hours, output_minutes)
    print(calculated_hours + calculated_days)
