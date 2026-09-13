
'''
Remove Duplicates from a Sorted Array

Theory:
Use two pointers to remove duplicate elements from a sorted
array without using extra space.

Working:
1. 'i' points to the last unique element.
2. 'j' traverses the array.
3. If nums[i] != nums[j], a new unique element is found.
4. Move 'i' forward and place the unique element there.
5. Continue until 'j' reaches the end.

Example:

[1, 1, 2, 2, 3, 3]

After removing duplicates:
[1, 2, 3]

Easy formula to remember:

i → Unique Element
j → Traverse
Compare → Move i → Swap
'''


def uique_element(nums):
    n = len(nums)

    # If only one element exists
    if n == 1:
        return 1

    # i points to the last unique element
    i = 0

    # j traverses the array
    j = i + 1

    # Traverse until j reaches the end
    while j < n:

        # Check for a new unique element
        if nums[i] != nums[j]:

            # Move to the next unique position
            i += 1

            # Place the unique element at i
            nums[i], nums[j] = nums[j], nums[i]

        # Move j to the next element
        j += 1

    # Return the number of unique elements
    return i + 1


nums = [1, 1, 2, 2, 3, 3, 4, 4]

result = uique_element(nums)

print(f"the duplicated element is removed and unique elements are {result}")


'''
Time Complexity:

O(n) → j traverses the array only once.

Space Complexity:

O(1) → only two pointers are used.

Important:
This approach works only when the array is sorted.

Remember:

Sorted Array + Two Pointers
= O(n) Time + O(1) Space
'''

