def lower_bound(nums, target):
    # Description: Finds the first index where nums[index] >= target.
    # TC: O(log n)
    # SC: O(1)

    n = len(nums)
    lower_bound = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lower_bound = mid
            high = mid - 1
        else:
            low = mid + 1

    return lower_bound

nums = [1, 2, 4, 4, 5, 7]
target = 4

result = lower_bound(nums, target)
print(result)  # 2
