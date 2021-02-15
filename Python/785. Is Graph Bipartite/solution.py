from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if graph == [[]]:
            return True
        g = {}
        for i, e in enumerate(graph):
            g[i] = e
        c = {}

        q = deque()
        visited = [0] * len(graph)
        for i in range(len(graph)):
            if visited[i] == 0:
                q.append(i)
                c[i] = 1
                while q:
                    curr = q.popleft()
                    visited[curr] = 1
                    for node in g[curr]:
                        if node not in c:
                            c[node] = - c[curr]
                            q.append(node)
                        else:
                            if c[node] == c[curr]:
                                return False

        return True