class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sList = list(s)
        stack = []

        for i, c in enumerate(sList):
            if c == "(":
                stack.append(i)
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    sList[i] = ""
        while stack:
            sList[stack.pop()] = ""

        return "".join(sList)

if __name__ == '__main__':
    s = Solution()
    assert s.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"