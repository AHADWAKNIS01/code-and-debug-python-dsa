
def linear_search(nums):
    n=len(nums)
    target=int(input("Tell what is your target:"))

    for i in range(n):
        if nums[i]==target:
            return i

    return -1


nums=[1,4,5,67,3,4,5,6]
print("your array is :",nums)

result=linear_search(nums)
print("element is present at the index",result)
