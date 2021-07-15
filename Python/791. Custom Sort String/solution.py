from collections import defaultdict


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        # time complexity : O(n)
        # Space complexity : O(n)
        dic = defaultdict(int)
        for char in str:
            dic[char] += 1
        res = []
        for char in order:
            if char in dic:
                res.append(char * dic[char])
                del dic[char]
        for k, v in dic.items():
            res.append(k * v)
        return "".join(res)
