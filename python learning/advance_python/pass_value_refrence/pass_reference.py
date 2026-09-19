def add_number(nums):
    nums.append(5)
    print(f"the value of x inside the block is ={nums}")



nums=[1,2,3,45,6]#this is an immutable object
add_number(nums)
print(f"Outside function={nums}")