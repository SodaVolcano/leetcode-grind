#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#


# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """naiive solution"""
        frontier = [[0, i] for i in graph[0]]
        paths = []
        while frontier:
            path = frontier.pop()
            if path[-1] == len(graph) - 1:
                paths.append(path)
                continue
            for i in graph[path[-1]]:
                frontier.append(path + [i])
        return paths


# @lc code=end
