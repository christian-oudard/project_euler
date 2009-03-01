days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

days_of_week = {
    0: 'monday',
    1: 'tuesday',
    2: 'wednesday',
    3: 'thursday',
    4: 'friday',
    5: 'saturday',
    6: 'sunday',
}

def is_leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False

def advance_date(date):
    year, month, day, weekday = date
    weekday = (weekday + 1) % 7
    day += 1
    if day > days_in_month[month]:
        month += 1
        day = 1
    if month > 12:
        year += 1
        month = 1
    return (year, month, day, weekday)

cur_date = (1900, 1, 1, 0) # Monday, January 1st, 1900
# advance to 1901
while cur_date < (1901,):
    cur_date = advance_date(cur_date)
# count all the sundays that are the first of the month in the 20th century
count = 0
while cur_date < (2001,):
    y, m, d, w = cur_date
    if d == 1 and w == 6:
        count += 1
    cur_date = advance_date(cur_date)

print(count)
