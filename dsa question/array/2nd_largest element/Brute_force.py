
'''
Second Largest Element in an Array

Description:
Find the second largest element in the array.

Approach:
1. First, find the largest element.
2. Then traverse the array again.
3. Ignore the largest element.
4. Find the maximum element among the remaining elements.
5. That value is the second largest element.

Example:
nums = [1, 2, 34, 5, 6, 4, 6, 8, 9, 3, 7, 8]

Largest element = 34
Second largest = 9


Time Complexity:
Best Case:    O(n)
Average Case: O(n)
Worst Case:   O(n)

Reason:
We traverse the array twice.
O(n) + O(n) = O(2n) = O(n)

Space Complexity: O(1)

Note:
This approach assumes that the array contains at least
two distinct elements.
'''

def largest_element(nums):
    n = len(nums)

    # -------------------------------------------------
    # Step 1: Find the largest element
    # -------------------------------------------------
    largest = nums[0]

    for i in range(0, n):
        largest = max(largest, nums[i])

    # -------------------------------------------------
    # Step 2: Find the largest element smaller than
    #         the largest element
    # -------------------------------------------------

    # Start with the first element instead of 0,
    # so negative numbers can also be handled.
    second_largest = float('-inf')

    for i in range(0, n):

        # Ignore the largest element
        if nums[i] < largest:

            # Keep the maximum value smaller than largest
            second_largest = max(nums[i], second_largest)

    return second_largest


nums = [1, 2, 34, 5, 6, 4, 6, 8, 9, 3, 7, 8]

second_largest = largest_element(nums)

print("second largest", second_largest)

