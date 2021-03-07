from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # bruteforce
        # words = list(set(words))
        # words.sort(key=lambda x: -len(x))
        # s = []
        # res = 0
        # for word in words:
        #     if s:
        #         for big in s:
        #             if big.endswith(word):
        #                 break
        #
        #         else:
        #             s.append(word)
        #             res += len(word) + 1
        #
        #     else:
        #         s.append(word)
        #         res += len(word) + 1
        #
        # return res

        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)