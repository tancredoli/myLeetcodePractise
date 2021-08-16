from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        len_s, len_t = len(s), len(t)

        c_t, c_cur = Counter(t), Counter()
        l, r = 0, 0
        res = ''
        while r < len(s):
            c_cur.update([s[r]])
            if r - l + 1 >= len_t and not (c_t - c_cur):
                while l <= r and r - l + 1 >= len_t and not (c_t - c_cur):
                    if res == '':
                        res = s[l:r + 1]
                    else:
                        if len(res) > r + 1 - l:
                            res = s[l:r + 1]
                    c_cur.subtract([s[l]])
                    l += 1

            r += 1
        return res