import calendar
def display_calendar(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal_str = cal.formatmonth(year, month)
    print(cal_str)
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
display_calendar(year, month)
