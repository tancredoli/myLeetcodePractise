class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res, bal = 0, 0
        for i,c in enumerate(S):
            if c == "(":
                bal += 1
            else:
                # remember to delete bal by 1 layer
                bal -= 1
                if S[i-1] == "(":
                    res += 1 << bal
        return res