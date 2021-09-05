from collections import defaultdict
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        count = N * [1]
        stsum = N * [0]
        g = defaultdict(set)
        for k, v in edges:
            g[k].add(v)
            g[v].add(k)

        def dfs(node=0, parent=None):
            for child in g[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    # very briliant
                    stsum[node] += stsum[child] + count[child]

        def dfs1(node=0, parent=None):
            for child in g[node]:
                if child != parent:
                    stsum[child] = stsum[node] - count[child] * 2 + N
                    dfs1(child, node)

        dfs()
        dfs1()
        return stsum