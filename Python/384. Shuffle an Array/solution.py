from random import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.copy = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.copy[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # Fisher - Yates Algorithm
        # time Complexity: O(n)
        l = len(self.nums)
        for i in range(l):
            swap_index = random.randint(i, l - 1)
            self.nums[i], self.nums[swap_index] = self.nums[swap_index], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()