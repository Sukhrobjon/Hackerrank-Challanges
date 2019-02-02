import calendar

# print out calendar
# print(calendar.TextCalendar(firstweekday=6).formatyear(2019))

def converting_date_to_weekday(month, day, year):
      return (list(calendar.day_name)[
          calendar.weekday(year, month, day)].upper())

month, day, year = input().split()
print(converting_date_to_weekday(int(month), int(day), int(year)))
# print(calendar.day_name[calendar.weekday(day[2], day[0], day[1])].upper())
# a, b, c = map(list(input()))
