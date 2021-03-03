from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                res.append(num)
        for i in range(1, n + 1):
            if i not in seen:
                res.append(i)

        return res