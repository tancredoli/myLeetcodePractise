from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            curr = [0] * 26
            base = ord('a')
            for char in word:
                curr[ord(char)-base] +=1
            dic[tuple(curr)].append(word)
        return list(dic.values())
    # concatenate