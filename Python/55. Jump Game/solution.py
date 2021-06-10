from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy approach
        fastest_index_pos = 0;
        for i, dis in enumerate(nums):
            if i > fastest_index_pos: return False
            fastest_index_pos = max(fastest_index_pos, i+dis);
        return True