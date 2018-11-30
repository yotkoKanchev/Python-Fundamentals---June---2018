import datetime

todays_date = datetime.date(2018, 8, 26)

data = input().split("-")

asked_date = datetime.date(int(data[0]), int(data[1]), int(data[2]))

delta = asked_date - todays_date

if todays_date == asked_date:
    print(f"Today date")

elif delta.days < 0:
   print(f"Passed")

else:
   print(f"{delta.days + 1} days left")



