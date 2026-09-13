#rotate array by 1 place
#indexing=0,1,2,3,4,5,6,7,8
#indexing in negative -8.-7,-6.-5,-4,-3-,-2-,-1
nums=[8,3,4,5,6,7,3,2]
n=len(nums)
nums[:]=[nums[-1]]+ nums[0:n-1]


print(nums)