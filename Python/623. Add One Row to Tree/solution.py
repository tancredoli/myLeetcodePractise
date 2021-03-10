# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(val=v, left=root)
            return new_root

        lv = 2
        q = [root]
        while q:
            length = len(q)
            for i in range(length):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if lv == d:
                    curr.left = TreeNode(val=v, left=curr.left)
                    curr.right = TreeNode(val=v, right=curr.right)
            if lv == d:
                break
            lv += 1
        return root