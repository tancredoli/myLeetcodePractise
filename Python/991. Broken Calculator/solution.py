class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        cnt = 0
        while X != Y:
            if Y > X:
                if Y % 2 == 0:
                    Y //= 2
                else:
                    Y += 1
                cnt += 1
            if Y < X:
                return cnt + X - Y

        return cnt