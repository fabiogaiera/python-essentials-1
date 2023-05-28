# LAB

def is_year_leap(year):
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    if is_year_leap(year) and month == 2:
        return 29
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28
    else:
        return 30


def day_of_year(year, month, day):
    count_days = 0
    count_month = 1

    while count_month < month:
        count_days += days_in_month(year, count_month)
        count_month += 1

    return count_days + day


print(day_of_year(2000, 12, 30))
