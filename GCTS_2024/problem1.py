"""
Fastival Booth Balance : 
"""

N = int(input())
booths = input().upper()[:N]

result = 0

for i in range(N-1):
    if(booths[i]==booths[i+1]):
        result=0
    else:
        result=1


print(result)

# Here we count total number of A => Gallary, 
print(f"Number of Galary : {booths.count('A')}")
print(f"Number of Music Studio : {booths.count('M')}")