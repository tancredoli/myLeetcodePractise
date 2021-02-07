# Definition for a binary tree node.

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = [root]
        res = [root.val]
        while q:
            length = len(q)
            for i in range(length):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if q:
                res.append(q[-1].val)
        return res