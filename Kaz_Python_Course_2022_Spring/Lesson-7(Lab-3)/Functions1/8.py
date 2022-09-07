def spy_game(nums): # 0 1 7 0 4 6 7
    l = []  # 0 0 
    for i in range(len(nums)):
        if nums[i] == 0 and (len(l) == 0 or len(l) == 1):
            l.append(0)
        if nums[i] == 7 and len(l) == 2:
            l.append(7)
        
    if len(l) == 3:
        print(True)
    else:
        print(False)

nums = [int(x) for x in input().split()]
spy_game(nums)

        