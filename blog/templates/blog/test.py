from datetime import date
import datetime
#13.1
now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
    print(now_str, file=output)
#13.2
with open('today.txt', 'rt') as input:
    today_string = input.read()
print(today_string)
#13.3
fmt = '%Y-%m-%d\n'
dt = datetime.datetime.strptime(today_string, fmt)
print("Year = " + str(dt.year))
print("Month = " + str(dt.month))
print("Day = " + str(dt.day))