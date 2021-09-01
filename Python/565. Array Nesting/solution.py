from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # with dfs
        # Space and time: both O(n)
        # mapping = {}
        # for i, num in enumerate(nums):
        #     mapping[i] = num
        #
        # self.visited = set()
        # self.result = 0
        #
        # def dfs(mapping, start, index, length):
        #     self.visited.add(index)
        #     if mapping[index] == start:
        #         self.result = max(length, self.result)
        #         return
        #     dfs(mapping, start, mapping[index], length + 1)
        #
        # for i in range(len(nums)):
        #     if i not in self.visited:
        #         dfs(mapping, i, i, 1)
        # return self.result

        # simple in-place loop
        # time: O(n) space: O(1)
        ans = 0
        for i in range(len(nums)):
            if nums[i] == -1: continue
            cnt = 0
            while nums[i]!= -1:
                cnt += 1
                nums[i], i = -1, nums[i]
            ans = max(cnt, ans)
        return ans