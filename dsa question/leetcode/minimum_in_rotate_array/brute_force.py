def min_in_rotate_array(nums):
    n=len(nums)
    mini=float("-int")

    for i in range(n):
        mini=min(mini,nums[i])

    return mini 