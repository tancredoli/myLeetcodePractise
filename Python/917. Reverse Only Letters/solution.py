class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # two pointers
        str_list = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if not str_list[l].isalpha():
                l += 1
                continue
            if not str_list[r].isalpha():
                r -= 1
                continue

            str_list[l], str_list[r] = str_list[r], str_list[l]
            l += 1
            r -= 1

        return "".join(str_list)