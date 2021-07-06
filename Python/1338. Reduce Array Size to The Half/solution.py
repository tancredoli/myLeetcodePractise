from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        length = len(arr)
        count_arr = sorted(list(count.values()),reverse = True)
        res = 0
        curr = 0
        for i, val in enumerate(count_arr):
            curr += val
            if curr >= length//2:
                return i + 1