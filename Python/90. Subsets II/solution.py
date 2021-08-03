from itertools import combinations
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)+1):
            curr = combinations(nums,i)
            for ele in curr:
                if ele not in res:
                    res.append(ele)
        return res