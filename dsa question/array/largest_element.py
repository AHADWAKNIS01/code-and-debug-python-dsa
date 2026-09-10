'''
largest element in the array'''



def largest_element(nums):
    n=len(nums)
    largest=nums[0]
    for i in range(0,n):
        largest=max(largest,nums[i])

    return largest


nums=[1,2,3,4,5,6,7,8,2,1,3]
resulth=largest_element(nums)
print("largest element is" ,resulth)