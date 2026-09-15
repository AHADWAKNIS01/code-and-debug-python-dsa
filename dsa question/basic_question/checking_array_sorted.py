
def check_sorted_array(nums):
    n=len(nums)

    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False

    return True



nums=[2,3,4,5,6,2,3,4,5]
result=check_sorted_array(nums)
print("does the array is sorted:",result)