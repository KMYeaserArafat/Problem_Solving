
minutes = ['zero','one','two','three','four','five',
           'six','seven','eight','nine','ten',
           'eleven','twelve','thirteen','fourteen',
           'fifteen','sixteen','seventeen','eighteen',
           'nineteen','twenty','twenty one', 'twenty two',
           'twenty three','twenty four','twenty five',
           'twenty six','twenty seven','twenty eight',
           'twenty nine', 'thirty']

hours = ['zero','one','two','three','four','five',
         'six','seven','eight','nine','ten','eleven','twelve']


H = int(input())
M = int(input())


if M==0:
    print(hours[H],"o' clock")
elif M==15:
    print("quater past", hours[H])
elif M==30:
    print("half past", hours[H])
elif M==45:
    if H==12:
        print("quater to",hours[1])
    else:
        print("quater to",hours[H+1])
elif M>0 and M<30:
    print(minutes[M],"minutes past",hours[H])
elif M>30 and M<60:
    if H==12:
        print(minutes[60-M],"minutes to",hours[1])
    else:
        print(minutes[60-M],"minutes to",hours[H+1])