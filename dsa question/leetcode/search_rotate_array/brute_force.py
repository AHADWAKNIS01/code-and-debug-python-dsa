def search_in_rotate_array(nums, target):
    # Description: Searches for target using linear search.
    # TC: O(n)
    # SC: O(1)

    n = len(nums)

    for i in range(n):
        if nums[i] == target:
            return i

    return -1


nums = [1, 2, 3, 3, 3, 3, 4, 5, 6, 7]
target = 4

print(search_in_rotate_array(nums, target))