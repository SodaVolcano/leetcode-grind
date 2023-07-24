#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#


# @lc code=start
class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        """
        each row has UNIQUE integers
        MINIMISE number of rows
        i.e. partition it such that each set have unique elements
        - find repeated elements and put in new list

        # Nah can't be bothered, have to check multiple lists too
        approach 1
            sort*nums( - easier to identify non-unique elements)
            then iterate through it and put duplicates in new list

        # Nah set difference doesn't work like I thought it would
        approach 2
            repeat until remainder is empty:
                sublist = set(nums)  # only unique elements
                remainder = set difference between nums and set(nums)

        approach 3:
            dictionary - num:count
            count up occurence of each number in nums
            n_counts = 0
            while True:
                ans.append([x for x in dict.keys() if dict[x] == n_counts])
                n_counts = True
        """
        return self.dict_approach(nums)

    def dict_approach(self, nums: list[int]) -> list[list[int]]:
        # Bad runtime and memory: ~65% & 16.6%
        # Count up frequency of each number and use freq count to construct subarrays
        counts = {}
        # Count how many times each number occur
        for i in nums:
            counts[i] = 0 if i not in counts.keys() else counts[i] + 1

        ans = []
        n_counts = 0
        while True:
            sublist = [num for num in counts.keys() if counts[num] >= n_counts]

            if not sublist:
                return ans

            ans.append(sublist)
            n_counts += 1

    def dict_approach2(self, nums: list[int]) -> list[list[int]]:
        # Great runtime ~86%, memory ~50%
        # Count up frequency of number and use frequency to index 2D answer array
        counts = {}
        ans = [[]]

        for i in nums:
            counts[i] = 0 if i not in counts.keys() else counts[i] + 1
            # counts == number of list in ans
            if counts[i] == len(ans):
                ans.append([i])
            else:
                ans[counts[i]].append(i)
        return ans


# @lc code=end
