from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_left, min_right = -1, min(nums)

        for i, num in enumerate(nums):
            if max_left < num: max_left = num
            if min_right == num and i != len(nums) - 1: min_right = min(nums[i + 1:])
            if max_left <= min_right:
                return i + 1