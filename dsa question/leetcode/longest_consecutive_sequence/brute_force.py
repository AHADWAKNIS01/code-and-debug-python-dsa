def longest_consecutive(nums):
    n=len(nums)
    max_count=0
    count=0
    for i in range(0,n):
        num=nums[i]
        count=1
        while num +1 in nums:
            count=count+1
            num+=1

        max_count=max(max_count,count)

    return max_count

nums = [100, 4, 200, 1, 3, 2]

# Call the function
result = longest_consecutive(nums)

# Display the result
print("The longest consecutive sequence is:", result)



        