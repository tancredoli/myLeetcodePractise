class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        def check(num):
            x, cnt = m - 1, 0
            for i in range(n):
                while x >= 0 and matrix[x][i] > num:
                    x -= 1
                cnt += (x + 1)
            return cnt

        l, r = matrix[0][0], matrix[m - 1][n - 1]

        # while l <= r:
        #     mid = (l+r)//2
        #     if check(mid) >= k:
        #         ans = mid
        #         r = mid-1
        #     else:
        #         l = mid+1

        while l <= r:
            mid = (l + r) // 2
            if check(mid) < k:
                l = mid + 1
            else:
                r = mid - 1
        return l