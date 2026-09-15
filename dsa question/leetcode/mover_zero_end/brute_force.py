def move_zero_end(nums):
    n=len(nums)

    temp=[]

    for i in range(0,n):
        if nums[i]!=0:
            temp.append(nums[i])

    temp_n=len(temp)
    for i in range(0,temp_n):
        nums[i]=temp[i]

    for i in range(temp_n,n):
        nums[i]=0

    print("the zeros have been pusht to end",nums)




nums=[1,2,3,4,5,6,0,4,5,0,3,0]

print("original array",nums)

move_zero_end(nums)

print("after peforming operation",nums)




        