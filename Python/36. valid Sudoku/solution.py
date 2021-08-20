from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            curr = set()
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in curr:
                        return False
                    else:
                        curr.add(board[i][j])

        for i in range(9):
            curr = set()
            for j in range(9):
                if board[j][i].isdigit():
                    if board[j][i] in curr:
                        return False
                    else:
                        curr.add(board[j][i])

        for m in range(0, 7, 3):
            for n in range(0, 7, 3):
                curr = set()
                for i in range(3):
                    for j in range(3):
                        if board[i + m][j + n].isdigit():
                            if board[i + m][j + n] in curr:
                                return False
                            else:
                                curr.add(board[i + m][j + n])

        return True