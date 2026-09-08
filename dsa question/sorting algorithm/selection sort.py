def selection_sort(nums):

    n = len(nums)

    for i in range(n):
        min_index = i

        # Find minimum element index from remaining array
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        # Swap minimum element with current position
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


arr = [1,2,3,6,7,8,5,4]

selection_sort(arr)

print(arr)