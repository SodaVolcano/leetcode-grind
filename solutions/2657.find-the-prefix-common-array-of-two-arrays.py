#
# @lc app=leetcode id=2657 lang=python3
#
# [2657] Find the Prefix Common Array of Two Arrays
#


# @lc code=start
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Both lists are permutations, so c[n] == n
        Imagine matching number in A and B as a set M
        at index i, we lose 2 numbers A[i+1] and B[i+1]
        keep a set of deletions to account how much M shrinks
        """
        deletions = set()
        C = [0] * (len(A) - 1) + [len(A)]

        for i in range(len(A) - 2, -1, -1):
            old_len = len(deletions)
            deletions.add(A[i + 1])
            deletions.add(B[i + 1])
            C[i] = C[i + 1] - (len(deletions) - old_len)
        C[0] = 0 if A[0] != B[0] else 1
        return C


# @lc code=end
