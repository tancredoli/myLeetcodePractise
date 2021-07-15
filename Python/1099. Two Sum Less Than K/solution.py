from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # time complextiy : O(nlog(n))
        nums = sorted(nums)
        l,r = 0 ,len(nums)-1
        res = -1
        while l < r:
            if nums[l] + nums[r] < k:
                res = max(res, nums[l] + nums[r])
                l +=1
            else:
                r -=1
        return res