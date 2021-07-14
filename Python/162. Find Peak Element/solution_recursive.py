from typing import List


class Solution:
    def bs(self, nums, l, r):
        # base case:
        if l == r:
            return l

        mid = (l + r) // 2

        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid

        if nums[mid] > nums[mid + 1]:
            return self.bs(nums, l, mid)
        else:
            return self.bs(nums, mid + 1, r)

    def findPeakElement(self, nums: List[int]) -> int:

        # Recursive Binary search
        return self.bs(nums, 0, len(nums)-1)