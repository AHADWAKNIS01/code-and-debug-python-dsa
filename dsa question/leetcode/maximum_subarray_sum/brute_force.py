
def max_sum(nums):
    n=len(nums)

    max_sum=float("-inf")
    for i in range(n):
        total=0
        for j in range(n):
            total=total+nums[j]
            max_sum=max(total,max_sum)

    return max_sum


nums=[1,2,4,5,6,7,5,-3,4,]
result=max_sum(nums)

print("the maximum sum is",result)

