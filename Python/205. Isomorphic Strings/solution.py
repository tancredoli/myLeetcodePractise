class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if s[i] in mapping:
                if t[i] != mapping[s[i]]:
                    return False
            else:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]
        return True