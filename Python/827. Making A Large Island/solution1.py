from collections import deque
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # time complexity: O(n^4)
        # space complexity: O(n^2)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n = len(grid)

        def bfs(x, y):
            q = deque([(x, y)])
            visited = [(x, y)]
            res = 0

            while q:
                curr = q.pop()
                res += 1
                for d in dirs:
                    if 0 <= curr[0] + d[0] < n and 0 <= curr[1] + d[1] < n and grid[curr[0] + d[0]][
                        curr[1] + d[1]] == 1 and (curr[0] + d[0], curr[1] + d[1]) not in visited:
                        q.appendleft((curr[0] + d[0], curr[1] + d[1]))
                        visited.append((curr[0] + d[0], curr[1] + d[1]))
            return res

        self.ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    self.ans = max(bfs(i, j), self.ans)
                    grid[i][j] = 0
        return self.ans if self.ans else n * n
