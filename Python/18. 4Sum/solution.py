from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # time complexity: O(n^3)
        # space : O(1)
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-3):
            for j in range(i+1,length-2):
                l = j + 1
                r = length -1
                curr_sum = nums[i] + nums[j]
                if target - curr_sum < nums[l] * 2:
                    continue
                while l < r:
                    if nums[l] + nums[r] == target - curr_sum:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        l +=1
                        r -=1
                    elif nums[l] + nums[r] > target - curr_sum:
                        r -=1
                    else:
                        l +=1
        return res