from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A or len(A) < 3:
            return 0
        res = 0
        l,r = 0,2
        diff = A[l+1] - A[l]
        while r < len(A):
            if diff == A[r] - A[r-1]:
                r += 1
            else:
                if r - l > 2:
                    sub = r - l -2
                    res += sub*(1+sub)//2
                r += 1
                l = r -2
                diff = A[l+1] - A[l]
        if r - l > 2:
            sub = r - l -2
            res += sub*(1+sub)//2
        return res

if __name__ == '__main__':
    s = Solution()
    assert s.numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert s.numberOfArithmeticSlices([1, 2, 3, 4, 5]) == 6
    assert s.numberOfArithmeticSlices([1, 2, 3, 4, 6]) == 3