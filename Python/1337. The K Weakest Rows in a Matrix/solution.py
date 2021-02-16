from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        transform = []
        for i in range(len(mat)):
            transform.append((sum(mat[i]), i))
        transform.sort()
        return [x[1] for x in transform][:k]
