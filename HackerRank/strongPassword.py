# Strong PassWord: 

def strongPassword(password,n):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    numberCount = 1
    lower_CaseCount = 1
    upper_caseCount= 1
    special_charactersCount = 1

    for char in password:
        if char in numbers:
            numberCount = 0
        elif char in lower_case:
            lower_CaseCount = 0
        elif char in upper_case:
            upper_caseCount = 0
        elif char in special_characters:
            special_charactersCount = 0

    maxData = max(6-n, numberCount+lower_CaseCount+upper_caseCount+special_charactersCount)
    return maxData


n = int(input())
password = str(input())[:n]
print(strongPassword(password,n))
