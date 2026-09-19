def sum_4(nums,target):
    n=len(nums)
    my_set=set()
    nums.sort()
    
    if n<4:
        return []
    
    for i in range(n-1):
        if i>0 and nums[i]== nums[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            
            k=j+1
            l=n-1
            while k<l:
                total=nums[i]+nums[j]+nums[k]+nums[l]
                if total ==target:
                    temp=[nums[i], nums[j], nums[k],nums[l]]
                    temp.sort()
                    my_set.add(tuple(temp))
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1

                    while l>k and nums[l]==nums[l+1]:
                        l-=1
                elif total < target:
                    k+=1
                else:
                    l-=1

              


    result=[]
    for i in my_set:
        result.append(list(i))

    return result

                        

   

nums = [1,0,-1,0,-2,2]
target = 0

print(sum_4(nums,target))
