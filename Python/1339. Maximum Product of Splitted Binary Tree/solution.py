# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs1(node):
            if node.left: dfs1(node.left)
            if node.right: dfs1(node.right)
            left_val = node.left.val if node.left else 0
            right_val = node.right.val if node.right else 0

            node.val = left_val + right_val + node.val

        dfs1(root)
        self.sum_, self.res = root.val, -float('inf')

        def dfs2(node):
            if self.res < (self.sum_ - node.val) * node.val:
                self.res = (self.sum_ - node.val) * node.val
            if node.left: dfs2(node.left)
            if node.right: dfs2(node.right)

        dfs2(root)
        return self.res % (10 ** 9 + 7)

