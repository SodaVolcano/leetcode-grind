#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#


# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        return self.argsort_approach(groupSizes)

    def dict_approach(self, groupSizes: List[int]) -> List[List[int]]:
        # Got worse runtime than argsort
        not_full = {}
        ans = []

        for i in range(len(groupSizes)):
            if groupSizes[i] == 1:
                ans.append([i])
            elif groupSizes[i] not in not_full.keys():
                not_full[groupSizes[i]] = [i]
            else:
                not_full[groupSizes[i]].append(i)
                if len(not_full[groupSizes[i]]) == groupSizes[i]:
                    ans.append(not_full[groupSizes[i]])
                    not_full[groupSizes[i]] = []
        return ans

    def argsort_approach(self, groupSizes: List[int]) -> List[List[int]]:
        indices = sorted(range(len(groupSizes)), key=lambda i: groupSizes[i])

        ans = []
        ptr = 0
        while ptr < len(groupSizes):
            ans.append(indices[ptr : ptr + groupSizes[indices[ptr]]])
            ptr += groupSizes[indices[ptr]]

        return ans


# @lc code=end
