from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxi = 0
        for i in c.keys():
            if i + 1 in c:
                maxi = max(maxi, c[i] + c[i + 1])
        return maxi


if __name__ == '__main__':
    s = Solution()
    assert s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5
    assert s.findLHS([1, 2, 3, 4]) == 2
    assert s.findLHS([1, 1, 1, 1]) == 0
