from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        raw_dict, col_dict, grid_dict = {}, {}, {}

        # inti
        for i in range(9):
            raw_dict[i] = set([str(i) for i in range(1, 10)])
            col_dict[i] = set([str(i) for i in range(1, 10)])
            grid_dict[i] = set([str(i) for i in range(1, 10)])

        def transform(r, c):
            # (r,c) -> 3 * (r)//3  + c // 3
            #
            return 3 * (r // 3) + (c // 3)

        # extration for the nums already in the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    raw_dict[r].remove(board[r][c])
                    col_dict[c].remove(board[r][c])
                    grid_dict[transform(r, c)].remove(board[r][c])

        def backtrack(board, r, c):
            # base case
            while board[r][c] != '.':
                c += 1
                if c == 9:
                    r += 1
                    if r == 9:
                        return True
                    c = 0

            for num in [str(i) for i in range(1, 10)]:
                if num in raw_dict[r] and num in col_dict[c] and num in grid_dict[transform(r, c)]:
                    board[r][c] = num
                    raw_dict[r].remove(num)
                    col_dict[c].remove(num)
                    grid_dict[transform(r, c)].remove(num)
                    if backtrack(board, r, c):
                        return True
                    raw_dict[r].add(num)
                    col_dict[c].add(num)
                    grid_dict[transform(r, c)].add(num)
                    board[r][c] = '.'

        backtrack(board, 0, 0)
        return board