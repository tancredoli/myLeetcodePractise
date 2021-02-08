from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [-1] * len(s)
        loc = []
        for i in range(len(s)):
            if s[i] == c:
                ans[i] = 0
                loc.append(i)
        p = 0

        for i in range(len(s)):
            if ans[i] != 0:
                while loc[p] < i and p + 1 < len(loc):
                    p += 1
                ans[i] = abs(i - loc[p])
                if p - 1 >= 0:
                    ans[i] = min(ans[i], abs(i - loc[p - 1]))
        return ans

if __name__ == '__main__':
    s = Solution()
    assert s.shortestToChar("loveleetcode", "e") == [3,2,1,0,1,0,0,1,2,2,1,0]