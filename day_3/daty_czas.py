from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2025-05-28
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2025-05-28 15:29:13.343382

print(time.year)  # 2025
print(today.day)  # 28

formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 28/05/2025

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 15:31
print(type(formated_time))  # <class 'str'>

object_datetime = datetime.now().strptime("28/05/2025", "%d/%m/%Y")
print(object_datetime)
print(type(object_datetime))  # <class 'datetime.datetime'>

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2025-05-29
