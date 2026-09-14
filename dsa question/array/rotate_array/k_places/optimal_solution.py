def k_place(nums):
    n=len(nums)
    k=int(input("enter no.of rotation:"))
    rotation=k % n

    nums[:]=nums[n-rotation:]+nums[:n-rotation]

    print("after rotation array is:",nums)

  


nums=[2,3,4,5,6,78,23,6]
print("before rotation:",nums)

k_place(nums)
print("after rotation:",nums)
