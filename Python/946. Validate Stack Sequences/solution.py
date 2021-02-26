from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # greedy
        if not pushed and not popped:
            return True
        s = []
        j = 0
        for i in range(len(pushed)):
            s.append(pushed[i])
            while s and j < len(pushed) and popped[j] == s[-1]:
                s.pop()
                j += 1

        return j == len(pushed)