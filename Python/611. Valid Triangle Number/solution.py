from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # edge case
        if len(nums) < 3:
            return 0
        res, length = 0, len(nums)
        nums = sorted(nums)                 # nLog(n)
        for i in range(length - 1, 0, -1):
            # O(n^2)
            l, r = 0, i - 1
            curr = nums[i]
            while l < r:
                if nums[l] + nums[r] > curr:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1
        return res