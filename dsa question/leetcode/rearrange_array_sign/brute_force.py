# Description:
# Rearrange the array by placing positive and negative elements
# alternately, starting with a positive element.
#
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)


def rearrage_array(nums):
    n = len(nums)

    negative = []  # Store negative elements
    positive = []  # Store positive elements

    # Separate positive and negative elements
    for i in range(n):

        # Check the actual element, not the index
        if nums[i] >= 0:
            positive.append(nums[i])
        else:
            negative.append(nums[i])

    # Place positive and negative elements alternately
    for i in range(len(negative)):

        nums[2 * i] = positive[i]       # Place positive element
        nums[(2 * i) + 1] = negative[i] # Place negative element

    # Return the rearranged array
    return nums


# Input array
nums = [1, -2, 3, 4, 5, -3, -2, -1]

# Call the function
result = rearrage_array(nums)

# Display the result
print("The rearranged array is:", result)