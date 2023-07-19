#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#


# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        for each n x n block, find
            max pillar in each ROW: max_row[i] = max(grid[i])
            max pillar in each COLUMN: max_col[i] = max([row[i] for row in grid])
        Then, max height for pillar at grid[i][j] without changing skylight is
            min(max_row[i], max_col[j]) - grid[i][j] (cliped to be >= 0)
        """
        row_max = [max(grid[i]) for i in range(len(grid))]
        col_max = [max(col) for col in zip(*grid)]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                height = min(row_max[i], col_max[j]) - grid[i][j]
                # Change to max increase speed by ~10% but decrease space by ~30%
                # count += max(height, 0)
                count += height if height > 0 else 0
        return count


# @lc code=end
