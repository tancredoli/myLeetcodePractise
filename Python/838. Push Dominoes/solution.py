class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l, r = 0, 0
        dominoes = list(dominoes)
        while r < len(dominoes):
            if dominoes[r] == '.':
                r += 1
                continue
            if dominoes[l] == 'R':
                if dominoes[r] == 'L':
                    cur_l, cur_r = l + 1, r - 1
                    while cur_l < cur_r:
                        dominoes[cur_l], dominoes[cur_r] = 'R', 'L'
                        cur_l += 1
                        cur_r -= 1
                else:
                    curr = l
                    while curr < r:
                        dominoes[curr] = 'R'
                        curr += 1

            else:
                if dominoes[r] == 'L':
                    curr = l
                    while curr < r:
                        dominoes[curr] = 'L'
                        curr += 1
            l = r
            r += 1

        if dominoes[l] == 'R':
            curr = l
            while curr < r:
                dominoes[curr] = 'R'
                curr += 1

        return "".join(dominoes)