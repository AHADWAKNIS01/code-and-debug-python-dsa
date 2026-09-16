def max_sum(nums):
    n=len(nums)
    max_value=0
    total=0

    for i in range(0,n):
        total=total+nums[i]
        max_value=max(max_value,total)

        if total<0:
            total=0

    return max_value


nums=[1,2,4,5,6,7,5,-3,4,]
result=max_sum(nums)

print("the maximum sum is",result)
