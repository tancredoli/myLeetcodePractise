# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node.left and not node.right: return node.val
            l = dfs(node.left) if node.left else 0
            r = dfs(node.right) if node.right else 0
            if l == 0: node.left = None
            if r == 0: node.right = None
            return l + r + node.val

        if dfs(root) == 0: root = None
        return root
