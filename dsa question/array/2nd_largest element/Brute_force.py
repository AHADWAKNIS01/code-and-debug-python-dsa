# ```python
'''
Second Largest Element Using Insertion Sort

Approach:
1. Sort the array using Insertion Sort.
2. After sorting in ascending order, the largest element
   will be at index n-1.
3. Therefore, the second largest element will be at index n-2.

Example:

Original:
[1, 2, 3, 4, 7, 8, 9, 5, 6, 66]

After sorting:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 66]

Largest = 66
Second largest = 9

Time Complexity:
Sorting using Insertion Sort = O(n²) average/worst case
Finding second largest     = O(1)

Overall Time Complexity:
O(n²)

Space Complexity:
O(1)
'''


def nums_sort(nums):

    # Find the total number of elements
    n = len(nums)

    # Start from index 1 because the first element
    # is considered already sorted
    for i in range(1, n):

        # Store the current element that we want
        # to place in its correct position
        key = nums[i]

        # Start comparing with the element just before key
        j = i - 1

        # Move elements greater than key one position
        # towards the right
        while j >= 0 and key < nums[j]:

            # Shift the larger element to the right
            nums[j + 1] = nums[j]

            # Move one position towards the left
            j -= 1

        # Insert key into its correct position
        nums[j + 1] = key

    # Return the sorted array
    return nums


def second_largest():

    # Input array
    nums = [1, 2, 3, 4, 7, 8, 9, 5, 6, 66]

    # Find the number of elements
    n = len(nums)

    # Sort the array using Insertion Sort
    sort_array = nums_sort(nums)

    # After ascending sorting:
    # index n-1 → largest
    # index n-2 → second largest
    return sort_array[n - 2]


# Call the function and print the result
print("second largest element is", second_largest())
# ```

# **Output:**

# ```text
# second largest element is 9
# ```

# ### 🧠 The main Insertion Sort logic

# Remember these 4 lines:

# ```python
# key = nums[i]             # Pick the element
# j = i - 1                 # Go backward
# while j >= 0 and key < nums[j]:
#     nums[j + 1] = nums[j] # Shift bigger element
#     j -= 1                 # Move backward
# nums[j + 1] = key         # Insert key
# ```

# **Pick → Compare backward → Shift bigger → Insert**

# And for your problem:

# **Sort → `n-2` → Second largest**.
