# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prew = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prew
            prew = curr
            curr = temp
        return prew