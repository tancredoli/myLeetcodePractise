# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        first,sec = head, head
        while first:
            remain = k
            curr_arr = []
            while first and remain:
                curr_arr.append(first.val)
                remain -=1
                first = first.next
            if remain == 0:
                while sec != first:
                    sec.val = curr_arr.pop()
                    sec = sec.next


        return head
