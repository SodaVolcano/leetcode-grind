#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        1. find max val in nums, and its INDEX
        2. use index to partition into
            left = nums[0:index]
            right = nums[index+1:]
        """

        def max_bin_tree(array: list[int]) -> Optional[TreeNode]:
            idx, max_val = max(enumerate(array), key=lambda x: x[1])
            return TreeNode(
                max_val,
                max_bin_tree(array[0:idx]) if array[0:idx] else None,
                max_bin_tree(array[idx + 1 :]) if array[idx + 1 :] else None,
            )

        return max_bin_tree(nums)


# @lc code=end
