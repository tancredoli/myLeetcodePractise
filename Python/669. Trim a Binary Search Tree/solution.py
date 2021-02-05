# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def trimHelper(self, par, node, low, high):
    #     if node.val >= low and node.val <= high:
    #         if node.left:
    #             self.trimHelper(node, node.left, low, high)
    #         if node.right:
    #             self.trimHelper(node, node.right, low, high)
    #     else:
    #         if node.left and node.left.val >= low and node.left.val <= high:
    #             if par.left == node:
    #                 par.left = node.left
    #                 self.trimHelper(par, par.left, low, high)
    #             if par.right == node:
    #                 par.right = node.left
    #                 self.trimHelper(par, par.right, low, high)
    #             return
    #         if node.right and node.right.val >= low and node.right.val <= high:
    #             if par.left == node:
    #                 par.left = node.right
    #                 self.trimHelper(par, par.left, low, high)
    #             if par.right == node:
    #                 par.right = node.right
    #                 self.trimHelper(par, par.right, low, high)
    #             return
    #         if par.left == node:
    #             par.left = None
    #         else:
    #             par.right = None

    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root