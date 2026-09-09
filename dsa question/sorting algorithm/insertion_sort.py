'''
Theory:
Insertion Sort is a sorting algorithm that takes one element at a time and places it in its correct position among the already sorted elements.

Think of arranging playing cards in your hand.

Working

Example:

[5|, 3, 4, 1]

Step 1: Take 3 → compare with 5 → 5 is bigger, so shift it.

[3, 5|, 4, 1]

Step 2: Take 4 → compare with 5 → shift 5.

[3, 4, 5,| 1]

Step 3: Take 1 → compare from right to left → shift 5, 4, 3.

[1, 3, 4, 5]
Easy formula to remember

Pick → Compare backward → Shift bigger → Insert

'''

def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]

        j=i-1

        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]

            j=-1

        nums[j+1]=key

    return nums

nums =[5,4,6,7,8,2]

print(insertion_sort(nums))
    


'''
Time Complexity:

Best case: O(n) → array is already sorted.
Average case: O(n²)
Worst case: O(n²) → array is in reverse order.

Space Complexity:

O(1) → it sorts the array in-place and uses only a few extra variables like key and j.

👉 Remember: Insertion Sort = Time: O(n²), Space: O(1).
'''