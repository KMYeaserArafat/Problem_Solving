#Designer PDF Viewer, 
import string

h = list(map(int,input().split()))
word = input()
wordSize = len(word)

st = string.ascii_lowercase

indexStore = []

for x in word:
    i = st.index(x)  #find out the word reall index number, 
    indexStore.append(h[i]) # here h[i] means collect this number in h list of index, 

maxIndex = max(indexStore)
result = wordSize*1*maxIndex
print(result)

