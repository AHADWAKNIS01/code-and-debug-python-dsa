def longest_consecutive_sequence(nums):
    n=len(nums)
    nums.sort()
    count = 0                     
    longest = 0                 
    last_smaller=float("-inf")
    for i in range(0,n):
        num=nums[i]

        if num-1==last_smaller:
            count+=1
            last_smaller=num

        # Ignore duplicate elements
        elif num == last_smaller:
            continue


        else: 
            count=1
            last_smaller=num


        longest=max(longest,count)
    return longest

nums = [100, 4, 200, 1, 3, 2]

result = longest_consecutive_sequence(nums)

print("The longest consecutive sequence is:", result)