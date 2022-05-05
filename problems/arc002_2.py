from datetime import datetime, timedelta

day = datetime.strptime(input(), "%Y/%m/%d")
one = timedelta(days=1)
while True:
    if day.year % (day.month * day.day) == 0:
        print(day.strftime("%Y/%m/%d"))
        exit()
    day += one
