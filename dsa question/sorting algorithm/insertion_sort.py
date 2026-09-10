# ```python
'''
Insertion Sort

Theory:
Insertion Sort is a sorting algorithm that takes one element
at a time and places it in its correct position among the
already sorted elements.

Think of arranging playing cards in your hand.

Working:
1. Start from the second element because the first element
   is considered already sorted.
2. Store the current element in 'key'.
3. Compare 'key' with the elements on its left.
4. If an element is greater than 'key', shift it one position
   to the right.
5. Continue moving backwards until the correct position
   for 'key' is found.
6. Insert 'key' into that position.

Easy formula to remember:

Pick → Compare Backward → Shift Bigger → Insert


Example:-

[5|, 4, 6, 7, 8, 2]

Pick 4:
[4, 5|, 6, 7, 8, 2]

Pick 6:
[4, 5, 6|, 7, 8, 2]

Pick 7:
[4, 5, 6, 7|, 8, 2]

Pick 8:
[4, 5, 6, 7, 8|, 2]

Pick 2:
[2, 4, 5, 6, 7, 8]


Time Complexity:

Best Case:    O(n)
Average Case: O(n²)
Worst Case:   O(n²)

Best Case:
The array is already sorted, so the while loop performs
very few operations for each element.

Worst Case:
The array is in reverse order. Every new element has to be
compared with and shifted past all previously sorted elements.

Space Complexity: O(1)

Reason:
Only a few extra variables such as 'key', 'i', and 'j'
are used.

In-place: Yes
Stable: Yes
'''


def insertion_sort(nums):

    # Get the total number of elements in the array
    n = len(nums)

    # Start from index 1 because the first element
    # at index 0 is considered already sorted
    for i in range(1, n):

        # Store the current element that we want
        # to place at its correct position
        key = nums[i]

        # Start comparing from the element immediately
        # before the key and move towards the left
        j = i - 1

        # Continue while:
        # 1. j is a valid index
        # 2. The previous element is greater than key
        #
        # If nums[j] > key, nums[j] needs to be shifted
        # one position to the right.
        while j >= 0 and nums[j] > key:

            # Shift the larger element one position
            # towards the right
            nums[j + 1] = nums[j]

            # Move one position towards the left
            # to continue comparing with previous elements
            j -= 1

        # Insert the key into its correct position
        # j + 1 is the position where key belongs
        nums[j + 1] = key

    # Return the sorted array
    return nums


# Input array
nums = [5, 4, 6, 7, 8, 2]

# Call the insertion sort function
result = insertion_sort(nums)

# Print the sorted array
print(result)


# **Output:**

# ```text
# [2, 4, 5, 6, 7, 8]
# ```

# ### ⭐ Most important part to remember

# ```python
# while j >= 0 and nums[j] > key:
#     nums[j + 1] = nums[j]
#     j -= 1

# nums[j + 1] = key
# ```

# Think:

# **Compare → Shift → Move Back → Insert**

# And complexity:

# **Best:** `O(n)`
# **Average:** `O(n²)`
# **Worst:** `O(n²)`
# **Space:** `O(1)`
