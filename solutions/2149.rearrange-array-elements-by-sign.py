#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#


# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        return [
            num
            for pair in zip([i for i in nums if i > 0], [i for i in nums if i < 0])
            for num in pair
        ]


# @lc code=end
