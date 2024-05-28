

password = str(input("Enter Password : ")).lower()
character = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['0','1','2','3','4','5','6','7','8','9']
oprator = ['#','@','$','%']

characterCount = 0
numberCount = 0
numberCount = 0
opratorCount = 0

for char in password:
    if char in character:
        characterCount+=1
    elif char in number:
        numberCount+=1
    elif char in oprator:
        opratorCount+=1

if opratorCount>=1 and numberCount>=1 and opratorCount>=1 and len(password)>=6:
    print("Strong Password")
else:
    print("Week Password !!")



