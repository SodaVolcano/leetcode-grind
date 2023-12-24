#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#


# @lc code=start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Notice how output vertices include all numbers not present as destination
        in an edge in the list of all edges, we just count all numbers not present
        as destination
        """
        reachable = set()
        for edge in edges:
            reachable.add(edge[1])
        return set([i for i in range(n)]).difference(reachable)


# @lc code=end
