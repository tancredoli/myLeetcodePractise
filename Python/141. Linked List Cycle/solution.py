# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        while head and head not in dic:
            dic[head] = 0
            head = head.next
        return True if head else False

if __name__ == '__main__':
    head = ListNode(3)
    pos = ListNode(2)
    head.next = pos
    pos.next = ListNode(0)
    pos.next.next = ListNode(-4)
    pos.next.next.next = pos
    s = Solution()
    assert s.hasCycle(head) == True

