#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root, None)

    def dfs(self, node: TreeNode, parent: TreeNode) -> int:
        # good speed improvement (~79%) but terrible space (~25%)
        count = 0

        if parent and not parent.val & 1:
            count += node.left.val if node.left else 0
            count += node.right.val if node.right else 0

        count += self.dfs(node.left, node) if node.left else 0
        count += self.dfs(node.right, node) if node.right else 0

        return count

    def bfs_approach(self, root: TreeNode) -> int:
        # Terrible runtime (~33%) but great memory (~94%)
        frontier = [root]
        count = 0
        while frontier:
            for node in frontier:
                # Sum all grandchildren if is even
                if not node.val & 1:
                    count += sum(
                        [n.right.val for n in [node.right, node.left] if n and n.right]
                        + [n.left.val for n in [node.right, node.left] if n and n.left]
                    )

            frontier = [node.left for node in frontier if node.left] + [
                node.right for node in frontier if node.right
            ]
        return count


# @lc code=end
