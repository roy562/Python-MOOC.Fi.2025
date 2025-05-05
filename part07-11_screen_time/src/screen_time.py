# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename:")
#filename = 'late_june.txt'

ip_starting_date = input("Starting date:")
#ip_starting_date = '24.6.2020'
one_day = timedelta(days=1)
start_date = datetime.strptime(ip_starting_date, "%d.%m.%Y")
start_date_str =  start_date.strftime('%d.%m.%Y')
end_date = start_date

days = int(input("How many days:"))
#days = 5
print("Please type in screen time in minutes on each day (TV computer mobile):")

total_screen_time = 0
daily_screen_times = {}

for i in range(days):
    end_date_str = end_date.strftime('%d.%m.%Y')
    screen_time_daily = input(f"Screen time {end_date_str}:")

    daily_screen_times[end_date_str] = screen_time_daily.replace(" ","/")
    daily_minutes = [int(i) for i in screen_time_daily.split(" ")]
    total_screen_time = total_screen_time+sum(daily_minutes)

    end_date+=one_day

with open(filename,'w') as op_file:
    op_file.write(f"Time period: {start_date_str}-{end_date_str}\n")
    op_file.write(f"Total minutes: {total_screen_time}\n")
    op_file.write(f"Average minutes: {total_screen_time/days}\n")
    for key,values in daily_screen_times.items():
        op_file.write(f"{key}: {values}\n")



print("Data stored in file", filename)