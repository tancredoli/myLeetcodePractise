from collections import Counter
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        c = Counter(candyType)
        x = len(list(c.keys()))
        return x if x <= n/2 else n//2