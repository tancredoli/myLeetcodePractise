from collections import Counter
from itertools import product
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # time complexity: O(n^2)
        # space complexity: O(n^2)
        m, n = len(grid), len(grid[0])
        neib_list = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        islands, count, ans = Counter(), 2, 0

        def dfs(t, i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != 1: return
            islands[t] += 1
            grid[i][j] = t
            for x, y in neib_list: dfs(t, x + i, y + j)

        for x, y in product(range(m), range(n)):
            if grid[x][y] == 1:
                dfs(count, x, y)
                count += 1

        for x, y in product(range(m), range(n)):
            if grid[x][y] != 0: continue
            neibs = set()
            for dx, dy in neib_list:
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] != 0:
                    neibs.add(grid[x + dx][y + dy])
            ans = max(ans, sum(islands[i] for i in neibs) + 1)

        return ans if ans else m * n
