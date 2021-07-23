# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.res = [] if root.val in to_delete else [root]

        def dfs(node):
            if not node: return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in to_delete:
                if node.left: self.res.append(node.left)
                if node.right: self.res.append(node.right)
                return None
            return node

        dfs(root)
        return self.res
