from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c_s, c_t = Counter(s), Counter(t)
        return True if len((c_s-c_t).items()) == 0 else False