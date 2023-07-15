#
# @lc app=leetcode id=1689 lang=python3
#
# [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
#


# @lc code=start
class Solution:
    def minPartitions(self, n: str) -> int:
        # return int(max(n))    # Initial answer

        # This is somehow faster???
        # I'm guessing max() casts each char to int and then sort so
        # there are some overhead?
        for i in range(9, 0, -1):
            if str(i) in n:
                return i
        return 1


# @lc code=end
