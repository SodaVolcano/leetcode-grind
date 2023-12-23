#
# @lc app=leetcode id=1551 lang=python3
#
# [1551] Minimum Operations to Make Array Equal
#


# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        """
        n = mean
        consider a = array[0:n//2], all its elements < n
        number of operations is sum of (difference of each element and n)
        Q: can we quickly calculate this sum?
        A. yes - if n is even, answer is len(a) ** 2
            if n is odd, answer is len(a) * (len(a) - 1)
        """
        if n % 2 == 0:
            return (n - (n // 2)) ** 2
        return (n - (n // 2)) * (n - (n // 2) - 1)


# @lc code=end
