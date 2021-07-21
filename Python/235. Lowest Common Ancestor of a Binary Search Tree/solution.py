# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:s,b = q, p
        else:
            s,b, = p, q
        queue = [root]
        length = len(queue)
        while queue:
            for i in range(length):
                curr = queue.pop()
                if curr.val > s.val and curr.val < b.val:
                    return curr
                if  curr.val == s.val or curr.val == b.val:
                    return curr
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            length = len(queue)
