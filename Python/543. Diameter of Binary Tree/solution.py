# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root: TreeNode) -> int:
        if not root:
            return 0

        _left = self.helper(root.left)
        _right = self.helper(root.right)
        self.res = max(self.res, _left + _right)

        return max(_left, _right) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 1 calculate the diameter crosing each node
        # 2 keep track of the longest diameter( just the value)
        # 3 after the traverse of tree return this longest diameter

        self.res = 0
        self.helper(root)

        return self.res