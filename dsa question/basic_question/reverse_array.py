def reverse_array(nums,left,right):
    

    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1




   

  


nums=[2,3,4,5,6,78,23,6]
print("before rotation",nums)
n=len(nums)
reverse_array(nums,0,n-1)

print("after  full rotation rotation ",nums)

reverse_array(nums,3,n-1)
print("after rotation 3",nums) 
