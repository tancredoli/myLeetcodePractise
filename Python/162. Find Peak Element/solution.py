from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # iterative binary search
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l