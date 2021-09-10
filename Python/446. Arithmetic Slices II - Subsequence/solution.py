from typing import Counter


class Solution:
    def numberOfArithmeticSlices(self, A):
        # dp Time: O(n^2) Space: O(n^2)
        total, n = 0, len(A)
        dp = [Counter() for item in A]
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += dp[j][diff] + 1
            total += sum(dp[i].values())
        return total - (n-1)*n//2   