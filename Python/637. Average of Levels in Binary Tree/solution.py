# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        queue = [root]

        while queue:
            length = len(queue)
            lv = 0
            for i in range(length):
                curr = queue.pop(0)
                lv += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(lv / length)
        return res