
'''
Remove Duplicates from an Array

Theory:
Remove duplicate elements from the array using a dictionary
(Hash Map).

Working:
1. Create an empty dictionary.
2. Store every element as a key.
3. Duplicate values automatically get ignored because
   dictionary keys are unique.
4. Traverse the dictionary and copy unique elements
   back into the array.

Example:

[1, 2, 3, 2, 1, 4]

Unique elements:
[1, 2, 3, 4]

Easy formula to remember:

Store → Unique Keys → Copy Back
'''


def removing_duplicates(nums):

    n = len(nums)

    # Dictionary stores only unique elements
    freq_map = {}

    # Add every element as a dictionary key
    for i in range(0, n):
        freq_map[nums[i]] = 0

    # Start inserting unique elements from index 0
    j = 0

    # Copy unique keys back into the array
    for k in freq_map:
        nums[j] = k
        j += 1

    return nums,j


nums = [1, 2, 3, 4, 5, 3, 4, 2, 1, 3, 4, 7, 88, 9]

result = removing_duplicates(nums)

print(f"the duplicated element is removed{result} and the number unque elemnet is ")


'''
Time Complexity:

O(n) → first loop takes O(n) and dictionary traversal
also takes O(n).

Overall: O(n)

Space Complexity:

O(n) → dictionary can store up to n unique elements.

Remember:

Hashing → O(n) Time + O(n) Space
'''

