def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
                print("Leap year.")
            else:
                return False
                print("Not leap year.")
        else:
            return True
    else:
        return False
        print("Not leap year.")


def days_in_month(year, month):
    """ Returns the days of the month and year passed as parameter """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = month_days[month-1]
    if is_leap(year) and month == 2:
        days += 1
    return days

# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
