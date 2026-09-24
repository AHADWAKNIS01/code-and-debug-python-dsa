class Solution:
    def lower_bound(self, nums, target):
        # Description: Finds the first index where nums[index] >= target.
        # TC: O(log n)
        # SC: O(1)

        n = len(nums)
        low = 0
        high = n - 1
        lb = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1

        return lb

    def upper_bound(self, nums, target):
        # Description: Finds the first index where nums[index] > target.
        # TC: O(log n)
        # SC: O(1)

        n = len(nums)
        low = 0
        high = n - 1
        ub = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1

        return ub

    def searchRange(self, nums, target):
        # Description: Counts the occurrences of target.
        # TC: O(log n)
        # SC: O(1)

        lb = self.lower_bound(nums, target)

        if lb == -1:
            return 0

        ub = self.upper_bound(nums, target)

        return ub - lb

nums = [1,2,3,3,3,3,4,5,6,7]
target = 3
solution = Solution()
print(solution.searchRange(nums, target))
