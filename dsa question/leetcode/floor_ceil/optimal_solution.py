def floor_ceil(nums, target):
    # Description: Finds the floor (largest value <= target) and ceil (smallest value >= target).
    # TC: O(log n)
    # SC: O(1)

    left = 0
    right = len(nums) - 1

    floor = -1
    ceil = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            floor = nums[mid]
            ceil = nums[mid]
            return floor, ceil

        elif nums[mid] > target:
            ceil = nums[mid]
            right = mid - 1

        else:
            floor = nums[mid]
            left = mid + 1

    return floor, ceil

nums = [1, 3, 5, 7, 9]
target = 6

result = floor_ceil(nums, target)

print(result)





