def has_33(nums): # 1 3 3 
    for i in range(len(nums)): # 0 1 2
        if i == len(nums) - 1:
            return False

        if nums[i] == 3 and nums[i+1] == 3:
            return  True
    
    return False

nums = [int(x) for x in input().split()]

if has_33(nums):
    print(True)
else:
    print(False)