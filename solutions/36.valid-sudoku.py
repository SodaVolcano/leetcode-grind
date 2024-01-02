#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counts = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                counts.extend(
                    [
                        (i, -1, board[i][j]),
                        (j, -2, board[i][j]),
                        (i // 3, j // 3, board[i][j]),
                    ]
                )
        return len(counts) == len(set(counts))

    def attempt_1(self, board: List[List[str]]) -> bool:
        """Naive solution"""
        squares = set()
        rows = [set()] * 9
        cols = [set()] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                old_s_len = len(squares)
                old_r_len = len(rows[i])
                old_c_len = len(cols[j])

                squares.add((i // 3, j // 3, board[i][j]))
                rows[i].add((i, board[i][j]))
                cols[j].add((j, board[i][j]))
                if (
                    len(squares) == old_s_len
                    or old_r_len == len(rows[i])
                    or old_c_len == len(cols[j])
                ):
                    return False

        return True


# @lc code=end
