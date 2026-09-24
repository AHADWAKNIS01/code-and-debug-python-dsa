def first_last_occurance(nums,target):
    n=len(nums)

    left=0
    
    first=-1
    last=-2
    for i in range(n):

        if nums[i]==target:
            if first==-1:
                first=i
        last=i

    return first,last
            
