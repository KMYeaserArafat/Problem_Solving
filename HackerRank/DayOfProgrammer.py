

def dayOfProgrammer(year):
     # default: NOT a leap year
    dm = "13.09."
    if year == 1918:
        # the transition year
        dm = "26.09."
    elif (year % 4 == 0) and (year < 1918 or year % 100 != 0 or year % 400 == 0):
        # a leap year
        dm = "12.09."
    return dm + str(year)



year = int(input())

print(dayOfProgrammer(year))