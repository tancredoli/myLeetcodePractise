class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # only three different results:
        # 1 - 0 means it is empty already
        # 2 - 1 means it is palindrome already
        # 3 - 2 means it is non-palindrome
        if not s:
            return 0
        elif s == s[::-1]:
            return 1
        else:
            return 2