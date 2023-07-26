#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#


# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        number of operations for box n is
            for each 1-bit, the number of distance between it and n

        1. get list of all 1-bit positions
            for "001011", pos = [2, 4, 5]
        2. ans[i] = abs(i - p) for p in pos   # Thought: dynamic programming?
        """
        pos = [idx for idx, bit in enumerate(boxes) if bit == "1"]
        return [sum(abs(i - p) for p in pos) for i in range(len(boxes))]


# @lc code=end
