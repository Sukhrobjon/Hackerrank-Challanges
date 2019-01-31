import calendar

# print out calendar
# print(calendar.TextCalendar(firstweekday=6).formatyear(2019))



day = [int(x) for x in input().split()]
print(list(calendar.day_name)[
      calendar.weekday(day[2], day[0], day[1])].upper())
print(calendar.day_name[calendar.weekday(day[2], day[0], day[1])].upper())
