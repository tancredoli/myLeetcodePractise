class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        nums = []
        lv = 1
        while num > 0:
            curr = num % 10
            if lv == 1:
                base_1 = 'I'
                base_5 = 'V'
                base_10 = 'X'
            elif lv == 2:
                base_1 = 'X'
                base_5 = 'L'
                base_10 = 'C'
            elif lv == 3:
                base_1 = 'C'
                base_5 = 'D'
                base_10 = 'M'
            elif lv == 4:
                base_1 = 'M'

            if curr > 0 and curr < 4:
                res = curr * base_1 + res
            elif curr == 4:
                res = base_1 + base_5 + res
            # elif curr == 5:
            #     res = base_t + res
            elif curr >= 5 and curr < 9:
                res = base_5 + (curr - 5) * base_1 + res
            elif curr == 9:
                res = base_1 + base_10 + res
            num //= 10

            lv += 1

        return res