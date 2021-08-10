class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        "0000011111111"
        "00000|111110101010"

        time: O(n)
        Space: O(1)
        '''
        cnt = s.count('1')
        res = cnt

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                cnt += 1
            else:
                cnt -= 1
            res = min(cnt, res)
        return res

