from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        res, pre = 0,0
        while l <= r:
            less = min(height[l],height[r])
            if pre < less:
                res = max(res, (r-l) * less )
            if less == height[l]:
                l += 1
            else:
                r -= 1
            pre = less
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49