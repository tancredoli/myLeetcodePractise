from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        for c in S:
            if c.isdigit():
                if not res:
                    res.append(c)
                else:
                    for i in range(len(res)):
                        res[i] += c
            else:
                if not res:
                    res.append(c.lower())
                    res.append(c.upper())
                else:
                    length = len(res)
                    for i in range(length):
                        curr = res[i]
                        res[i] += c.upper()
                        res.append(curr + c.lower())
        return res