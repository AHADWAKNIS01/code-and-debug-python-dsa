def missing_number(nums):
    n=len(nums)

    for i in range(0,n+1):
        if i not in nums:
            print("the number not in array is :",i)

            return


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

missing_number(nums)
    

        