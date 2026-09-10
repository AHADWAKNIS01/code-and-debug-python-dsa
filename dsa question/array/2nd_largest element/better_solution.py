

'''
Second Largest Element

Theory:
Find the second largest element without sorting the array.

Working:
1. First find the largest element.
2. Traverse the array again.
3. Ignore the largest element.
4. Find the maximum among the remaining elements.

Example:

[2, 3, 4, 5, 6, 1, 7, 8, 9]

Largest = 9
Second largest = 8

Easy formula to remember:

Find Largest → Ignore Largest → Find Maximum
'''


def second_largest(nums):
    n = len(nums)

    # Initialize both values
    largest = float("-inf")
    second_largest = float("-inf")

    # Find the largest element
    for i in range(0, n):
        largest = max(largest, nums[i])

    # Find the largest element except largest
    for i in range(0, n):
        if nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]

    return second_largest


nums = [2, 3, 4, 5, 6, 1, 7, 8, 9]

result = second_largest(nums)

print("second largest is =", result)


'''
Time Complexity:

O(n) → array is traversed twice.
O(n) + O(n) = O(n)

Space Complexity:

O(1) → only a few variables are used.

Remember:
Second Largest = O(n) Time + O(1) Space
'''

