#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#


# @lc code=start
import bisect


class Solution:
    def countPoints(
        self, points: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        """
        FIND n_points inside circle (x, y, r) in each query!

        1. formula of circle is
            (x - a)^2 + (y - b)^2 = r^2
        2. Point (a, b) is in circle (x, y, r) iff
            (a - x)^2 + (b - y)^2 <= r^2
        3. so, for each query i,
            4. ans[i] = sum([points_in_circle(p) for p in points])

        improvement: for EACH QUERY (not the whole question)
            so... there MUST be some preprocessing on the POINTS
                sort by x?
                    [x0, x1, x2, x3, x4]
                    can exclude any x-coordinates outside x - r and x + r
        """
        points = sorted(points, key=lambda x: x[0])
        ans = []

        for q in queries:
            # Exclude points outside the 2 * r range on x-axis
            low, up = self.binary_search_interval(points, q[0] - q[2], q[0] + q[2])

            accum = 0
            for i in range(low, up + 1):
                accum += (
                    1
                    if (points[i][0] - q[0]) ** 2 + (points[i][1] - q[1]) ** 2
                    <= q[2] ** 2
                    else 0
                )
            ans.append(accum)
        return ans

    def binary_search_interval(self, arr: list[list[int]], lower: int, upper: int):
        lower_idx = bisect.bisect_right(arr, lower - 1, key=lambda x: x[0]) - 1
        upper_idx = bisect.bisect_left(arr, upper + 1, key=lambda x: x[0])

        return (
            lower_idx if lower_idx > 0 else 0,
            upper_idx if upper_idx < len(arr) else len(arr) - 1,
        )


# @lc code=end
