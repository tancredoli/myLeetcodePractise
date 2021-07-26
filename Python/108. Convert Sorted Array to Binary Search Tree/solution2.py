# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildTree(nums):
            if not nums: return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            mid = len(nums) // 2
            curr = TreeNode(nums[mid])
            curr.left = buildTree(nums[:mid])
            if mid + 1 < len(nums):
                curr.right = buildTree(nums[mid + 1:])
            return curr

        return buildTree(nums)
