from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        return sum((c1-c2).values())

if __name__ == '__main__':
    s = Solution()
    assert s.minSteps("leetcode","practice") == 5