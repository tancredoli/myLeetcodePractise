# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root: return False
        self._set = set()

        def dfs(node):
            if not node:
                return

            if node.val in self._set:
                return True

            self._set.add(k - node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)

