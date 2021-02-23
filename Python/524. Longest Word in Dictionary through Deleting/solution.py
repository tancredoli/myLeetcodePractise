from typing import List


class Solution:
    def isSubstring(self, s: str, t: str):
        s_i, t_i = 0, 0

        while s_i < len(s) and t_i < len(t):
            if s[s_i] == t[t_i]:
                t_i += 1
            s_i += 1
        return t_i == len(t)

    def findLongestWord(self, s: str, d: List[str]) -> str:
        if not s or not d:
            return ""

        #         dic = defaultdict(list)
        #         for i in range(len(s)):
        #             dic[s[i]].append(i)

        #         q = []

        #         self.curr_res = -1

        #         def backtrack(dic, word, curr):
        #             if len(curr) == len(word):
        #                 self.curr_res = max(self.curr_res, curr[-1]- curr[0])
        #                 return

        #             for pos in dic[word[len(curr)]]:
        #                 if len(curr) == 0 or (len(curr)!=0 and pos > curr[-1]):
        #                     curr.append(pos)
        #                     backtrack(dic, word, curr)
        #                     curr.pop()
        res = ""
        for word in d:
            if self.isSubstring(s, word):
                res = min(res, word, key=lambda x: (-len(x), x))
        return res