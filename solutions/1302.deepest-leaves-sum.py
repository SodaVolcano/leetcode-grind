#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # keep list of frontier[] = [root]
        # if node has NULL children, add to sum[]
        # if exists node in frontier[] with non-NULL, discard sum[]
        # If first node is non-NULL, don't add to sum at all (DEEPEST = False)
        # replace frontier[] with nodes with non-NULL

        frontier: list = [root]  # List of nodes to explore
        while True:
            node_sum = 0
            deepest = True
            new_frontier: list = []

            for node in frontier:
                # Is leaf and (assumed) deepest level, add to sum
                if node.left is None and node.right is None and deepest:
                    node_sum += node.val
                # Deeper leaf exists, reset sum
                else:
                    deepest = False
                    new_frontier.append(node.left) if node.left != None else None
                    new_frontier.append(node.right) if node.right != None else None
            if deepest:
                break

            frontier = new_frontier
        return node_sum


# @lc code=end
