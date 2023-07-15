#
# @lc app=leetcode id=793 lang=python3
#
# [793] Preimage Size of Factorial Zeroes Function
#

"""
k = number of zeros
find number of integers with that many trailing zeros

so... 

"""


# @lc code=start
class Solution:
    @staticmethod
    def count_trailing_zeros(n):
        count = 0
        i = 5
        while n // i >= 1:
            count += n // i
            i *= 5
        return count

    def preimageSizeFZF(self, k: int) -> int:
        if k == 0:
            return 5
        x = 5 * k
        while self.count_trailing_zeros(x) != k:
            x -= 5
            if self.count_trailing_zeros(x) < k:
                return 0

        return 5


# @lc code=end
