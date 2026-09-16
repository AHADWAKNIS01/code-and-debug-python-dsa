# Description:
# Find two elements in the array whose sum is equal to the target.
# Use a hash map to store each element and its index.
# Return the indices of the two elements if a pair is found.
#
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)


def sum_of_target(nums, target):
    n = len(nums)

    hash_map = {}  # Stores element as key and its index as value

    # Traverse through the array
    for i in range(n):

        # Calculate the value needed to reach the target
        remaining = target - nums[i]

        # Check if the required value already exists
        if remaining in hash_map:
            return [hash_map[remaining], i]

        # Store the current element and its index
        hash_map[nums[i]] = i

    # Return None if no pair is found
    return None


# Input array
nums = [1, 2, 3, 5, 6, 4, 8, 9, 48, 12, 1, 3, 15, 4]

# Target sum
target = 100

# Call the function
result = sum_of_target(nums, target)

# Display the result
print("The indices are:", result)