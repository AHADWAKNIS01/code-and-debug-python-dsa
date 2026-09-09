'''
Quick Sort — Working

Theory:
Quick Sort is a Divide and Conquer algorithm.

It works using a pivot.

Working

Example:

[5, 3, 8, 1, 2]
Choose a pivot → 5
Put smaller elements on the left and larger on the right:
[3, 1, 2]  5  [8]
Repeat the same process for the left and right parts:
[1, 2, 3]  5  [8]
Combine:
[1, 2, 3, 5, 8]
Remember

Quick Sort = Choose Pivot → Partition → Recursively Sort Left & Right

Average time: O(n log n)
Worst time: O(n²)
Space: O(log n) average (recursion stack)
'''

def partition(nums,low,high):
    pivot= nums[low]
    i=low 
    j=high

    #moving i until we gt the eelement geter then pivot
    while i<j:
        while i<= high-1 and nums[i]<=pivot:
            i+=1


        #travsing the j until get the element less the pivoto
        while j>low and nums[j]>pivot:
            j-=1

        if i<j:
            nums[i],nums[j]=nums[j],nums[i]


    nums[low],nums[j]=nums[j],nums[low]


    return j



def quick_sort(nums,low,high):

    #if more then one element
    if low<high:
    #finding the pivot correct postion
        p_index=partition(nums,low,high)


        #sort left side
        quick_sort(nums,low,p_index-1)

        #sort right side
        quick_sort(nums,p_index+1,high)


nums = [5, 3, 8, 1, 2, 7]

print("Before sorting:", nums)

quick_sort(nums, 0, len(nums) - 1)

print("After sorting:", nums)     





    





