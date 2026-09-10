
'''
Largest Element in an Array

Description:
Find the largest element present in the array by traversing
each element one by one and comparing it with the current
largest value.

Approach:
1. Assume the first element is the largest.
2. Traverse through the entire array.
3. Compare each element with 'largest'.
4. If the current element is greater, update 'largest'.
5. Return the largest element.

Time Complexity:
Best Case:    O(n)
Average Case: O(n)
Worst Case:   O(n)

Reason:
We check every element of the array, so the loop runs n times.

Space Complexity: O(1)
Reason:
Only one extra variable 'largest' is used.
'''

def largest_element(nums):
    n = len(nums)

    # Assume the first element is the largest initially
    largest = nums[0]

    # Traverse through all elements of the array
    for i in range(0, n):

        # Compare current element with the largest found so far
        largest = max(largest, nums[i])

    # Return the largest element
    return largest


nums = [1, 2, 3, 4, 5, 6, 7, 8, 2, 1, 3]

resulth = largest_element(nums)

print("largest element is", resulth)
