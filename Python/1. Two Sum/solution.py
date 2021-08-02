from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time O(n)
        # Space O(n)
        dic = {}
        for i, num in enumerate(nums):
            m = target - num
            if m not in dic:
                dic[num] = i
            else:
                return [dic[m], i]