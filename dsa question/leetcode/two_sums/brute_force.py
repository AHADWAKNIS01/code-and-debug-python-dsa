# Description:
# Find two elements in the array whose sum is equal to the target.
# Return the indices of those two elements.
#
# Time Complexity (TC): O(n^2)
# Space Complexity (SC): O(1)


def sum_of_target(nums, target):
    n = len(nums)

    # Check every possible pair of elements
    for i in range(n - 1):

        # Compare the current element with the remaining elements
        for j in range(i + 1, n):

            # Check if the pair sum is equal to the target
            if nums[i] + nums[j] == target:
                return i, j

    # Return None if no pair is found
    return None


# Input array
nums = [1, 2, 3, 5, 6, 4, 8, 9, 48, 12, 1, 3, 15, 4]

# Target sum
target = 10

# Call the function
result = sum_of_target(nums, target)

# Display the result
print("The indices are:", result)