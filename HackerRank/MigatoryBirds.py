
from collections import Counter

n = int(input().strip())

arr = list(map(int,input().rstrip().split()))

freequency = Counter(arr)
print("Frequency", freequency)
print("Max : ", max(freequency, key=freequency.get))

