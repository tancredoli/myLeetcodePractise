from collections import defaultdict
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes = [0] + releaseTimes
        dic = defaultdict(int)
        pos = []
        maximum = 0
        for i, c in enumerate(keysPressed):
            if dic[c] < (releaseTimes[i + 1] - releaseTimes[i]):
                dic[c] = releaseTimes[i + 1] - releaseTimes[i]
            if dic[c] > maximum:
                pos = [c]
                maximum = dic[c]
            elif dic[c] == maximum:
                pos.append(c)
        return max(pos)

