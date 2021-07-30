from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m, n = len(mat), len(mat[0])
        res = [[0 for i in range(n)] for j in range(m)]
        # visited = [[0 for i in range(n)] for j in range(m)]
        # self.curr = float('inf')
        #
        # def backtrack(x, y, step):
        #     if mat[x][y] == 0:
        #         self.curr = min(self.curr, step)
        #         return
        #
        #     for d in dirs:
        #         if d[0] + x < m and d[0] + x >= 0 and d[1] + y < n and d[1] + y >= 0 and visited[d[0] + x][
        #             d[1] + y] == 0:
        #             visited[d[0] + x][d[1] + y] = 1
        #             backtrack(d[0] + x, d[1] + y, step + 1)
        #             visited[d[0] + x][d[1] + y] = 0

        def bfs(x, y):
            q = deque([(x, y)])
            visited = []
            cnt = 0
            while q:
                cnt += 1
                length = len(q)
                for i in range(length):
                    x, y = q.pop()
                    visited.append((x, y))
                    for d in dirs:
                        if m > d[0] + x >= 0 and n > d[1] + y >= 0:
                            if mat[d[0] + x][d[1] + y] == 0:
                                return cnt
                            else:
                                if (d[0] + x, d[1] + y) not in visited:
                                    q.appendleft((d[0] + x, d[1] + y))

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    res[i][j] = bfs(i, j)

        return res