from collections import deque


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = deque()
        num1, num2, carry = list(num1), list(num2), 0

        while num1 or num2 or carry:
            add_1 = int(num1.pop()) if num1 else 0
            add_2 = int(num2.pop()) if num2 else 0
            cur_sum = add_1 + add_2 + carry
            if cur_sum >= 10:
                carry = 1
                cur_sum -= 10
            else:
                carry = 0
            ans.appendleft(str(cur_sum))
        return "".join(ans)
