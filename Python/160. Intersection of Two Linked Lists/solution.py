class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # solution 1 T: O(n) S: O(1)
        currA, currB = headA, headB
        while currA != currB:
            currA = headB if not currA else currA.next
            currB = headA if not currB else currB.next
        return currA

        # solution 2 T: O(n) S: O(n)
        seen = set()
        while headA and headB:
            if headA not in seen:
                seen.add(headA)
            else:
                return headA

            if headB not in seen:
                seen.add(headB)
            else:
                return headB
            seen.add(headB)
            seen.add(headA)

            headA = headA.next
            headB = headB.next
        while headA:
            if headA not in seen:
                seen.add(headA)
            else:
                return headA
            headA = headA.next
        while headB:
            if headB not in seen:
                seen.add(headB)
            else:
                return headB
            headB = headB.next

        return None



