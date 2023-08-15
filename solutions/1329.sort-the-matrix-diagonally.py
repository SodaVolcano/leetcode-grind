#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#


# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        arrays = [[] for _ in range(len(mat) + len(mat[0]) - 1)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arrays[i - j].append(mat[i][j])

        arrays = [sorted(array, reverse=True) for array in arrays]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = arrays[i - j].pop()
        return mat


# @lc code=end
