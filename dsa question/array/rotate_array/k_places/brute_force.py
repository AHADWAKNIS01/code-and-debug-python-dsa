def k_place(nums):
    n=len(nums)
    k=int(input("enter no.of rotation"))
    rotation=k % n

    for _ in range(0,rotation):
        last_element=nums.pop()
        nums.insert(0,last_element)
    print(nums)


nums=[2,3,4,5,6,78,23,6]
print("before rotation",nums)


result=k_place(nums)
print("after rotation",result)
