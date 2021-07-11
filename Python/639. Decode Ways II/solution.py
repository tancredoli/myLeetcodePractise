class Solution:
    def numDecodings(self, s: str) -> int:
        m = 10 ** 9 + 7
        dp = [1] * (len(s) + 1)
        if s[0] == '0':
            dp[1] = 0
        elif s[0] == '*':
            dp[1] = 9
        for i in range(1, len(s)):
            if s[i] == '*':
                dp[i + 1] = 9 * dp[i] % m
                if s[i - 1] == '1':
                    dp[i + 1] = (dp[i + 1] + 9 * dp[i - 1]) % m
                elif s[i - 1] == '2':
                    dp[i + 1] = (dp[i + 1] + 6 * dp[i - 1]) % m
                elif s[i - 1] == '*':
                    dp[i + 1] = (dp[i + 1] + 15 * dp[i - 1]) % m
            else:
                dp[i + 1] = dp[i] if s[i] != '0' else 0
                if s[i - 1] == '1':
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % m
                elif s[i - 1] == '2' and s[i] <= '6':
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % m
                elif s[i - 1] == '*':
                    if s[i] <= '6':
                        timer = 2
                    else:
                        timer = 1
                    dp[i + 1] = (dp[i + 1] + timer * dp[i - 1]) % m

        return int(dp[len(s)])


