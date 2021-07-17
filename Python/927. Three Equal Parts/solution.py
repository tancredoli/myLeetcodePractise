from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        c = sum(arr)
        if c % 3 != 0:
            return [-1, -1]

        if c == 0:
            return [0, len(arr) - 1]

        cnt = 0
        interval = []
        for i, item in enumerate(arr):
            if item == 1:
                cnt += 1
                if cnt in [1, c // 3 + 1, 2 * c // 3 + 1]:
                    interval.append(i)
                if cnt in [c // 3, 2 * c // 3, c]:
                    interval.append(i)

        if not (arr[interval[0]:interval[1]] == arr[interval[2]:interval[3]] == arr[interval[4]:interval[5]]):
            return [-1, -1]
        x = interval[2] - interval[1] - 1
        y = interval[4] - interval[3] - 1
        z = len(arr) - interval[5] - 1

        if z > x or z > y:
            return [-1, -1]

        return [interval[1] + z, interval[3] + z + 1]

        print(interval)
