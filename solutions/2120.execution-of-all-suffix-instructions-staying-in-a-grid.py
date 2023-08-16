#
# @lc app=leetcode id=2120 lang=python3
#
# [2120] Execution of All Suffix Instructions Staying in a Grid
#


# @lc code=start
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # Brute force >:(
        ans = [0 for _ in range(len(s))]

        for i in range(len(s)):
            start = startPos[::]

            for direction in s[i:]:
                match direction:
                    case "U":
                        start[0] -= 1
                    case "D":
                        start[0] += 1
                    case "R":
                        start[1] += 1
                    case "L":
                        start[1] -= 1

                if start[0] >= 0 and start[0] < n and start[1] >= 0 and start[1] < n:
                    ans[i] += 1
                else:
                    break
        return ans


# @lc code=end
