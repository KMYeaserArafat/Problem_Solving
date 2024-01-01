while(i<n):
            j = i+1
            while(j<n):
                if(arr[i]==arr[j]):
                    count+=1
                    i+=1
                    return count
                elif(arr[i]<arr[j]):
                    i+=2