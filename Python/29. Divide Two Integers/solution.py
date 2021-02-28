class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # genius
        positive = (dividend < 0) is (divisor < 0)

        # transfer to positive integer
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0

        # binary search until dividend is less than divisor
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)