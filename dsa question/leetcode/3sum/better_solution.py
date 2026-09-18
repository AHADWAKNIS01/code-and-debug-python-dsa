
def sum_3(nums):
    n=len(nums)
    result=set()

    for i in range(n-2):
        my_set=set()
        for j in range(i+1,n):
            third=-(nums[i]+nums[j])
            if third in my_set:
                temp=[nums[i],nums[j],third]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[j])

    return [list(ans) for ans in result]


nums = [-1, 0, 1, 2, -1, -4]

print(sum_3(nums))
