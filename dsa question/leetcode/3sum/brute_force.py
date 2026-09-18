def sum_3(nums):
    n=len(nums)
    my_set=set()

    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] == 0:

                    temp=[nums[i],nums[j], nums[k]]
                    temp.sort()

                    my_set.add((tuple(temp)))

    return [list(ans)  for ans in my_set]


nums = [-1, 0, 1, 2, -1, -4]

print(sum_3(nums))

# Output:
# [[-1, -1, 2], [-1, 0, 1]]

