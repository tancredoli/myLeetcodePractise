# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.res = []

        def dfs(curr, s):
            if not curr: return
            s.append(curr.val)
            if not curr.left and not curr.right and sum(s) == targetSum:
                self.res.append(s[:])
            if curr.left:
                dfs(curr.left, s)
            if curr.right:
                dfs(curr.right, s)
            s.pop()

        dfs(root, [])
        return self.res
