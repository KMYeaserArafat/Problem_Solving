
# Mars-Exploration, 

def marsExploration(s):
    count = 0

    for x in range(0,len(s),3):
        if s[x] != 'S':
            count+=1
        elif s[x+1] !='O':
            count+=1
        elif s[x+2] !='S':
            count+=1
    
    return count

    # for char in s:
    #    if char != 'S' and char !='O':
    #        count+=1
    
    # return count


s = str(input()).upper()
print(marsExploration(s))