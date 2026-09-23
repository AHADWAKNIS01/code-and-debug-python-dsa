def binary_search(nums, low, high, target):
    # Description: Recursively searches for target in a sorted array.
    # TC: O(log n)
    # SC: O(log n) - recursion stack

    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        return binary_search(nums, mid + 1, high, target)

    else:
        return binary_search(nums, low, mid - 1, target)



nums = [1, 3, 5, 7, 9, 11, 13]

print(binary_search(nums, 0, len(nums) - 1, 9))