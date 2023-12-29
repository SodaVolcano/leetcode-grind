#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = self.traverseBST(root)
        return self.constructBST(nodes)

    def constructBST(self, array):
        if len(array) == 0:
            return None
        mid = len(array) // 2
        mid_node = TreeNode(array[mid].val)
        mid_node.left = self.constructBST(array[:mid])
        mid_node.right = self.constructBST(array[mid + 1 :])
        return mid_node

    def traverseBST(self, node):
        left_right = []
        for child in [node.left, node.right]:
            if child is None:
                left_right.append([])
            else:
                left_right.append(self.traverseBST(child))
        return left_right[0] + [node] + left_right[1]


# @lc code=end
