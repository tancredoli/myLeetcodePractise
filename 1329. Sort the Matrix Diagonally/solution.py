from collections import defaultdict
from typing import List

def diagonalSort(mat: List[List[int]]) -> List[List[int]]:
    # 1. initalization
    m, n = len(mat), len(mat[0])
    dic = defaultdict(list)

    # 2. save items on the same diagonal into the dict
    for i in range(m):
        for j in range(n):
            dic[i - j].append(mat[i][j])

    # 3. sort the list in the dict
    for l in dic:
        dic[l].sort()

    # 4. put the sorted items back to the matrix
    for i in range(m):
        for j in range(n):
            mat[i][j] = dic[i - j].pop(0)

    return mat


if __name__ == '__main__':
    print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))