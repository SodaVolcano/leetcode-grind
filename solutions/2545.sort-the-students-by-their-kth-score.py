#
# @lc app=leetcode id=2545 lang=python3
#
# [2545] Sort the Students by Their Kth Score
#


# @lc code=start
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # What kind of question is this???? just a sorting question???
        # -key: 75% runtime, 91% memory
        # reverse=True: 35% runtime, 67% memory
        #     but the fastest solution used reverse=True????
        #     wtf???
        #     okay running same function multiple times gives different
        #     runtime and memory, wow
        return sorted(score, key=lambda i: -i[k])


# @lc code=end
