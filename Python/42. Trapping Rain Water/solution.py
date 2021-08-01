from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers
        # time complexity O(n)
        # space complexity O(1)
        if not height:
            return 0
        l, r, res = 0, len(height) - 1, 0

        # while height[l] == 0:
        #     l += 1
        # while height[r] == 0:
        #     r -= 1
        l_max, r_max = height[l], height[r]
        while l < r:

            if height[l] < height[r]:
                if height[l] > l_max:
                    l_max = height[l]
                else:
                    res += l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    res += r_max - height[r]
                r -= 1
        return res
