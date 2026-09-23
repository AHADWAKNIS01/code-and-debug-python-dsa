def upper_bound(nums, target):
    # Description: Finds the first index where nums[index] > target.
    # TC: O(log n)
    # SC: O(1)

    n = len(nums)
    upper_bound = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            upper_bound = mid
            high = mid - 1
        else:
            low = mid + 1

    return upper_bound