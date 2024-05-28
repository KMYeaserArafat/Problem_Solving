#Library-Fine, 

def LibraryFine(d1,d2,m1,m2,y1,y2):
    fine = 0

    if(d1<d2 and m1==m2 and y1==y2):
        return fine
    elif(d1>d2 and m1==m2 and y1==y2):
        lateDate = d1-d2
        fine = lateDate*15
        return fine
    elif(d1<=d2 or d1>=d2 and m1>m2 and y1==y2):
        lateMonth = m1-m2
        fine = lateMonth*500
        return fine
    elif(d1<=d2 or d1>=d2 and m1>=m2 or m1<=m2 and y1>y2):
        fine = 10000
        return fine


d1,m1,y1 = map(int,input().split()) #submit date
d2,m2,y2 = map(int,input().split()) #due Date
print(LibraryFine(d1,d2,m1,m2,y1,y2))







