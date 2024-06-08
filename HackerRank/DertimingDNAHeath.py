# # Determining DNA Heath



n = int(input())
for x in range(n):
    genes = list(input().split())
    health = list(map(int,input().split()))[:len(genes)]

    for y in range(0,int(input())):
        dStart,dEnd, d = input().split()
        # Implement start here,
        gList = []
        hList = []
        for z in range(int(dStart), int(dEnd)+1):
            gList.append(genes[z])
            hList.append(health[z])
            DataSet = list(zip(gList,hList))
            value_dic = dict(DataSet)
            sumData = sum(value_dic[x] for x in d)
    
         

print(sumData)


        