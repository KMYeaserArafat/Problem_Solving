
import calendar

def AutoCalender():
    requiredYear = int(input("Enter Year : "))
    AutoGenerateCalender = calendar.TextCalendar(firstweekday=7).formatyear(requiredYear)
    print(AutoGenerateCalender)