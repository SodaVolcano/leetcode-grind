#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        First element in array is root, and array is split into elem < root and elem > root
        [root, (<, <, <, ...), (>, >, ...)]
        1. split arary into 3: root, <, and >
        """
        return self.bstSubTree(preorder)

    def bstSubTree(self, array):
        root = TreeNode(array[0])
        if len(array) == 1:
            return root

        l, h = 1, len(array) - 1
        idx = len(array)
        while l <= h:
            mid = l + (h - l) // 2
            if array[mid] > array[0]:
                idx = mid
                h = mid - 1
            else:
                l = mid + 1

        root.left = self.bstSubTree(array[1:idx]) if array[1:idx] else None
        root.right = self.bstSubTree(array[idx:]) if array[idx:] else None
        return root


# @lc code=end
