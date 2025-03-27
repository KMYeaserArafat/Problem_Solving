

def contains_Duplication(nums):
    return  len(nums) != len(set(nums))


nums = list(map(int,input().split()))
print(contains_Duplication(nums))

