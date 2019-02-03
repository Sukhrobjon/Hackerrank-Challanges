import calendar

def converting_date_to_weekday(month, day, year):
      return (list(calendar.day_name)[
          calendar.weekday(year, month, day)].upper())

month, day, year = input().split()
print(converting_date_to_weekday(int(month), int(day), int(year)))

