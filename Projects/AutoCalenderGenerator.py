
import calendar

requiredYear = int(input("Enter Year : "))

AutoGenerateCalender = calendar.TextCalendar(firstweekday=7).formatmonth(requiredYear)
print(AutoGenerateCalender)