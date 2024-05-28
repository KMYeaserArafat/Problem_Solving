#PassWord-Crack, 

password = "Hello#2024"
chacters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
opretor = "#@&$*%"
PassDataStore = []

for x in password.lower():
    if x in chacters:
        PassDataStore.append(x)
    elif x in numbers:
        PassDataStore.append(x)
    elif x in opretor:
        PassDataStore.append(x)
        
Data = ''.join(PassDataStore)

if Data==password.lower():
    print("Password Match")
    print("Password : ",password)
else:
    print("Password not Match")

