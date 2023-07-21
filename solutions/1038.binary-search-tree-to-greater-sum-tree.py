#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        Since values are UNIQUE...
            a > b iff a is_right_child_of b
        Do DFS, starting from RIGHT node

        """
        self.gst(root)
        return root

    def gst(self, node: TreeNode, val: int = 0) -> int:
        # how has this taken me this long to solve

        if node.right is None and node.left is None:
            node.val += val
            return node.val

        max_val = 0
        if node.right is not None:
            node.val += self.gst(node.right, val)
            max_val = node.val

        # Edge case
        node.val += val if node.right is None else 0

        if node.left is not None:
            max_val = self.gst(node.left, node.val)
        return max_val


# @lc code=end
