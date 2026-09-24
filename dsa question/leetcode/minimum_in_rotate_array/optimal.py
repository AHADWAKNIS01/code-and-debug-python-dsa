def min_in_rotate_array(nums):
    n=len(nums)
    mini=float("-int")

    left=0
    right=n-1

    while left<=right:
        mid=(left+right)//2

        if nums[mid]<=nums[right]:
            right=mid-1
            mini=min(mini,nums[mid])
        else:
            mini=min(mini,nums[left])
            left=mid+1

    return mini
            
