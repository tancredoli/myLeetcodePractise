#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res ='' 
        _sum = sum(shifts)
        for i in range(len(s)):
            curr = _sum
            res += chr(ord('a') + (ord(s[i]) - ord('a')  + curr) % 26)
            _sum -= shifts[i]
        return res


# @lc code=end

