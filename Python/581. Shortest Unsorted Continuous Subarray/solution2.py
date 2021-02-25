
# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        l,r = 0, len(nums)-1
        while l <= r and sorted_nums[l] == nums[l] :
            l+=1
        while l <= r and sorted_nums[r] == nums[r]:
            r-=1
        return r-l + 1