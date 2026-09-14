def reverse_array(nums,left,right):
    

    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1




   

  


nums=[2,3,4,5,6,78,23,6]
print("before rotation",nums)

n=len(nums)
rotation=int(input("enter no.of rotation need:"))
reverse_array(nums,n-rotation,n-1) #reverse last part
reverse_array(nums,0,n-rotation-1)#reverse initail part
reverse_array(nums,0,n-1)
print("after rotation form the {rotation} ",nums)



