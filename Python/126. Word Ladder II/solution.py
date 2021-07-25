from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        # this backtracking solution got a TLE
        def check(w_1, w_2):
            if not w_1 or not w_2 or len(w_1) != len(w_2):
                return False
            s_ = 0
            for i, char in enumerate(w_1):
                if char != w_2[i]:
                    s_ += 1
                    if s_ > 1:
                        return False

            return True if s_ == 1 else False

        self.res = []
        self.dic = {}
        for word in wordList:
            self.dic[word] = 1

        def backtrack(curr):
            if curr[-1] == endWord:
                if self.res:
                    if len(self.res[0]) > len(curr):
                        self.res = [curr[:]]
                    elif len(self.res[0]) == len(curr):
                        self.res.append(curr[:])
                else:
                    self.res = [curr[:]]

            for w in wordList:
                if self.dic[w] and check(w, curr[-1]):
                    self.dic[w] = 0
                    curr.append(w)
                    backtrack(curr)
                    curr.pop()
                    self.dic[w] = 1

        backtrack([beginWord])
        return self.res
