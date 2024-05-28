
#Beautiful-Binary-String, 
import re
def beautifulBinaryString(b):
    data = re.findall(r'010',b)

    return len(data)


n = int(input())
b = input().strip()[:n]
print(beautifulBinaryString(b))