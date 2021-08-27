class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for curr in preorder.split(','):
            stack.append(curr)
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3].isdigit():
                for i in range(3):
                    stack.pop()
                stack.append('#')
        return True if stack == ['#'] else False
