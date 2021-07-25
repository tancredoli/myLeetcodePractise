class Solution:
    def findIntegers(self, n: int) -> int: \
            # naive approach : not passed
        # def check(s):
        #     for i in range(len(s)-1):
        #         if s[i] == '1' and s[i+1] == '1':
        #             return True
        #     return False
        # rs = 0
        # for x in range(n+1):
        #     if not check(bin(x)[2:]):
        #         rs+=1
        # return rs

        # Fibonacci numbers
        # Time complexity: O(logn)
        s = bin(n + 1)[2:]
        dp = [1, 2] + [0] * (len(s) - 2)
        for i in range(2, len(s)):
            dp[i] = dp[i - 1] + dp[i - 2]
        rs = 0
        for i in range(len(s)):
            if i > 1 and s[i - 1] == '1' and s[i - 2] == '1' and s[i] == '1':
                break
            if s[i] == '1':
                rs += dp[len(s) - i - 1]
        return rs
