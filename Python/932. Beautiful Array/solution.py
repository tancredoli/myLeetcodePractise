from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def dfs(nums):
            if len(nums) <= 2:
                return nums
            return dfs(nums[::2]) + dfs(nums[1::2])

        arr = [i for i in range(1, n + 1)]
        return dfs(arr)


