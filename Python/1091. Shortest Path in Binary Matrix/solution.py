from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] == 1 or grid[0][0] == 1:
            return -1
        res = 1
        height = len(grid)
        width = len(grid[0])
        dire = [(0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1), (1, -1), (1, 0), (1, 1)]

        queue = deque([[0, 0]])

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr[0] == height - 1 and curr[1] == width - 1:
                    return res

                for d in dire:
                    _curr = [curr[0] + d[0], curr[1] + d[1]]
                    if _curr[0] >= 0 and _curr[0] < height and _curr[1] >= 0 and _curr[1] < width and grid[_curr[0]][
                        _curr[1]] == 0:
                        grid[_curr[0]][_curr[1]] = -1
                        queue.append(_curr)

            res += 1

        return -1