from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        closest = float('inf')
        for i in range(length - 2):
            l, r = i + 1, length - 1
            c_target = target - nums[i]
            while l < r:
                curr = nums[l] + nums[r]
                if curr == c_target:
                    return target
                if abs(curr - c_target) < abs(closest - target):
                    closest = curr + nums[i]
                if curr > c_target:
                    r -= 1
                elif curr < c_target:
                    l += 1
        return closest
