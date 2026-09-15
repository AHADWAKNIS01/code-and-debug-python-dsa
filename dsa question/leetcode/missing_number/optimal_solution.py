def optimal_solution(nums):
    n=len(nums)
    freq={}


    for i in range(n):
        freq[i]=0


    for i in nums:
        freq[i]=1

    for key,value in freq.items():
        if value==0:
            print("the missing number is ",key)




nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

optimal_solution(nums)
    

