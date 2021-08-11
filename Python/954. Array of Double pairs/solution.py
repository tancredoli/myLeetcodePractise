from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        arr.sort(key=abs)
        for item in arr:
            if cnt[item] == 0: continue
            if cnt[2 * item] == 0: return False
            cnt[item] -= 1
            cnt[2 * item] -= 1
        return True
        # this method got a TLE
#         arr.sort()
#         index = 0
#         for i in range(len(arr)):
#             if arr[i] >= 0:
#                 index = i
#                 break
#             if i== len(arr) - 1:
#                 index = len(arr)
#         front = arr[:index]
#         end = arr[index:]
#         end.reverse()
#         def check(a):
#             if not a:
#                 return True

#             while a:
#                 curr = a.pop()
#                 if 2*curr in a:
#                     a.remove(2*curr)
#                 else:
#                     return False
#             return True
#         return True if check(front) and check(end) else False


