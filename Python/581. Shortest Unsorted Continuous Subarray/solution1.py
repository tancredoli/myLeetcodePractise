from typing import List

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = []
        l,r = len(nums)-1,0
        for i in range(len(nums)):
            while s and nums[s[-1]] > nums[i]:
                l = min(l,s.pop())
            s.append(i)
        s.clear()

        for i in range(len(nums)-1,-1,-1):
            while s and nums[s[-1]] < nums[i]:
                r = max(r, s.pop())
            s.append(i)

        return r-l+1 if r > l else 0