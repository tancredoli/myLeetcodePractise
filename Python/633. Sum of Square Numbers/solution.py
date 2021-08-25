from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # brute-force solution
        bdy = int(c**.5) + 1
        for i in range(bdy):
            cur = (c - i**2) ** 0.5
            # if cur % 1 == 0 :
            if cur == int(cur):
                return True
        return False

    def judgeSquareSumTwoP(self, c: int) -> bool:
        # two-pointers approach
        l, r = 0, int(sqrt(c)) + 1

        while l <= r:
            curr = l ** 2 + r ** 2
            if curr == c:
                return True
            elif curr > c:
                r -= 1
            else:
                l += 1
        return False