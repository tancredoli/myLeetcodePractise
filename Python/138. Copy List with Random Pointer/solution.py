
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # if not head:
        #     return None
        # dic, mapping = {} , {}
        # curr = head
        # _curr = Node(curr.val)
        # _head = _curr
        # i = 0
        # dic[i] = (curr, _curr)
        # mapping[curr] = i
        # while curr:
        #     i+=1
        #     if curr.next:
        #         _curr.next = Node(curr.next.val)
        #         dic[i] = (curr.next, _curr.next)
        #         mapping[curr.next] = i
        #     _curr = _curr.next
        #     curr = curr.next
        # _curr = _head
        # curr = head
        # i = 0
        # while curr:
        #     if curr.random:
        #         idx = mapping[curr.random]
        #         dic[i][1].random = dic[idx][1]
        #     curr = curr.next
        #     i+=1
        # return _head

        # edge case
        if not head:
            return head

        # 1. creat weaved linked list
        curr = head
        while curr:
            temp = curr.next
            curr.next = Node(curr.val, temp)
            curr = curr.next.next

        # 2. assign random ptr for cloned nodes
        curr = head
        while curr:
            ptr = curr.random
            if ptr:
                curr.next.random = ptr.next
            curr = curr.next.next

        # 3. seperate cloned nodes from original list
        curr = head
        res = curr.next
        while curr:
            temp = curr.next
            curr.next = curr.next.next
            if temp.next:
                temp.next = temp.next.next
            curr = curr.next
        return res

