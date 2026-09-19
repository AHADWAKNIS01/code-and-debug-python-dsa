def sum_4(nums,target):
    n=len(nums)
    my_set=set()
    
    
    if n<4:
        return []
    
    for i in range(n-2):
        for j in range(i+1,n-1):
            hash_set=set()
            for k in range(j+1,n):
                fourth=target-(nums[i] + nums[j] + nums[k])
                if fourth in hash_set:
                    temp=[nums[i], nums[j], nums[k],fourth]
                    temp.sort()

                    my_set.add(tuple(temp))
                hash_set.add(nums[k])

    result=[]
    for i in my_set:
        result.append(list(i))

    return result

                        

   

nums = [1,0,-1,0,-2,2]
target = 0

print(sum_4(nums,target))
