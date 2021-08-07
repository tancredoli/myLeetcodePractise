"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            length = len(q)
            cur_list = []
            for i in range(length):
                curr = q.pop()
                cur_list.append(curr.val)
                if curr.children:
                    q.extendleft(curr.children)
            res.append(cur_list)
        return res

