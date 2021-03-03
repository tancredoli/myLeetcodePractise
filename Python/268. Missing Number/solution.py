from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_withx = (+ len(nums)) * (len(nums) + 1) // 2
        sum_withoutx = sum(nums)

        return sum_withx - sum_withoutx