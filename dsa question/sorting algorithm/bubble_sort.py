'''
bubble sort:-basically the comparing the first elemnt with all and placing at correct palce similary 2nd placing at correct affter comparing
'''


def bubble_sort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            
        
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

    return nums


nums=[5,6,7,3,2,1]
print(bubble_sort(nums))

    