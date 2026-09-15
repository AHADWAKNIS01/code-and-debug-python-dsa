def move_zero_end(nums):
    n=len(nums)

    if n==1:
        return

    i=0
    while i<n:
        if nums[i]==0:
            break
        i+=1

    if i==n:
        return

    j=i+1
    while(j<n):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1

    return

   





nums=[1,2,3,4,5,6,0,4,5,0,3,0]

print("original array",nums)

move_zero_end(nums)


print("after peforming operation",nums)




          

