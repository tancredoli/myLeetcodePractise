# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root):
        if not root:
            return
        self.helper(root.right)
        self.sum += root.val
        root.val = self.sum
        self.helper(root.left)
        return

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.helper(root)
        return root

