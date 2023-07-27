#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Observation: LEAF will always be counted!

    avg = (node.val + node.left.total + node.right.total) / n_nodes
    if node.val == avg, count ++
    """

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # great memory usage (99.17%, how????) but mid speed (52.08%)
        # Top runtime answer have the exact algorithm as me, wtf
        # Running it a second time gives 24.58% memory and 67.08% runtime
        # so I'm guessing those metrics are more or less random
        ans = 0

        def subtree_avg(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0

            total_left, n_nodes_left = subtree_avg(node.left)
            total_right, n_nodes_right = subtree_avg(node.right)

            total = node.val + total_left + total_right
            n_nodes = 1 + n_nodes_left + n_nodes_right
            if node.val == total // n_nodes:
                nonlocal ans
                ans += 1
            return total, n_nodes

        subtree_avg(root)
        return ans


# @lc code=end
