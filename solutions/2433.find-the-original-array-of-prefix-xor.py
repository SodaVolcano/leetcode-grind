#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#
import itertools


# @lc code=start
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # Not much improvement, 72.82% speed and 75.66% memory (why worse memory?)
        return [pref[0]] + [pref[i + 1] ^ pref[i] for i in range(0, len(pref) - 1)]

    def approach2(self, pref: List[int]) -> List[int]:
        # Great speed improvement ~71.43%, great memory 86.24%
        return [pref[0]] + [pref[i] ^ pref[i - 1] for i in range(len(pref) - 1, 0, -1)][
            ::-1
        ]

    def approach1(self, pref: List[int]) -> List[int]:
        # Great memory ~99.82% but terrible time 18.17%
        for i in range(len(pref) - 1, 0, -1):
            pref[i] ^= pref[i - 1]
        return pref


# @lc code=end
