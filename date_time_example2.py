from datetime import datetime

week_day = datetime.today().weekday()
week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_zone = input("Are you in the US? (Yes/No): ")
if time_zone.lower() == "yes":
    print(week_days[week_day+1])
if time_zone.lower() == "no":
    print('Bye')

