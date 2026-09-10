
'''
Second Largest Element

Theory:
Find the second largest element by traversing the array only once.

Working:
1. Keep track of the largest element.
2. Keep track of the second largest element.
3. If current element is greater than first_largest,
   move first_largest to second_largest.
4. Otherwise, if it is greater than second_largest,
   update second_largest.

Example:

[2, 3, 4, 5, 6, 1, 7, 8, 9]

First largest = 9
Second largest = 8

Easy formula to remember:

Compare → Update Largest → Update Second Largest
'''


def second_largest(nums):

    # Start with the smallest possible value
    first_largest = float("-inf")
    second_largest = float("-inf")

    n = len(nums)

    # Traverse the array only once
    for i in range(0, n):

        # New largest element found
        if nums[i] > first_largest:

            # Previous largest becomes second largest
            second_largest = first_largest

            # Update largest
            first_largest = nums[i]

        # Update second largest if needed
        elif nums[i] > second_largest and nums[i] != first_largest:
            second_largest = nums[i]

    return second_largest


nums = [2, 3, 4, 5, 6, 1, 7, 8, 9]

result = second_largest(nums)

print("second largest is =", result)


'''
Time Complexity:

O(n) → array is traversed only once.

Space Complexity:

O(1) → only two extra variables are used.

Remember:
Single Pass = O(n) Time + O(1) Space
'''