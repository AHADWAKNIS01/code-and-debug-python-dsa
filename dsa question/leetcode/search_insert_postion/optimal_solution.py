
def search_insert_position(nums, target):
    # Description: Finds the first index where nums[index] >= target.
    # TC: O(log n)
    # SC: O(1)

    n = len(nums)

    left = 0
    right = n - 1
    lower_bound = n

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            lower_bound = mid
            right = mid - 1
        else:
            left = mid + 1

    return lower_bound


nums = [1, 3, 5, 6]
target = 7