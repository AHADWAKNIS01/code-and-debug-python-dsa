def sum_4(nums,target):
    n=len(nums)
    my_set=set()
    temp=0
    if n<4:
        return []
    
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp=[nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()

                        my_set.add(tuple(temp))

                        

    return [list(ans) for ans in my_set]

nums = [1,0,-1,0,-2,2]
target = 0

print(sum_4(nums,target))
