class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def seperate(num):
            add1, add2 = num.split('+')
            return int(add1), int(add2.split('i')[0])

        mul11, mul12 = seperate(num1)
        mul21, mul22 = seperate(num2)

        new_add1 = mul11 * mul21 - mul12 * mul22
        new_add2 = mul11 * mul22 + mul12 * mul21
        return str(new_add1) + '+' + str(new_add2) + 'i'