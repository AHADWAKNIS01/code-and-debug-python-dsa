
'''
Bubble Sort

Description:
Bubble Sort is a sorting algorithm that repeatedly compares
adjacent elements and swaps them if they are in the wrong order.

In each pass, the largest unsorted element moves to its
correct position at the end of the unsorted part.

Example:
[5, 6, 7, 3, 2, 1]

After sorting:
[1, 2, 3, 5, 6, 7]


Approach:
1. Compare adjacent elements.
2. If the left element is greater than the right element,
   swap them.
3. After each pass, the largest element reaches its
   correct position.
4. 'is_swap' checks whether any swapping happened.
5. If no swap happens, the array is already sorted,
   so we stop early.


Time Complexity:
Best Case:    O(n)
Average Case: O(n²)
Worst Case:   O(n²)

Best Case:
When the array is already sorted, no swaps occur.
'is_swap' remains False, so the loop stops after one pass.

Average/Worst Case:
Multiple passes and comparisons are required.

Space Complexity: O(1)

In-place: Yes
Stable: Yes
'''

def bubble_sort(nums):
    n = len(nums)

    # Start from the second-last index and move backwards.
    # 'i' represents the last index of the unsorted portion.
    for i in range(n - 2, -1, -1):

        # Used to detect whether any swapping happened
        is_swap = False

        # Compare adjacent elements from index 0 to i
        for j in range(0, i + 1):

            # If elements are in the wrong order, swap them
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

                # A swap occurred
                is_swap = True

        # If no swap happened, the array is already sorted
        if is_swap == False:
            break

    return nums


nums = [5, 6, 7, 3, 2, 1]

print(bubble_sort(nums))
