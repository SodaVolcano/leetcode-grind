#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#


# @lc code=start
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = sum([len(i) for i in garbage])
        seen_glass = False
        seen_metal = False
        seen_paper = False

        for i in range(len(garbage) - 1, -1, -1):
            if "G" in garbage[i] and not seen_glass:
                seen_glass = True
                ans += sum(travel[0:i])
            if "P" in garbage[i] and not seen_paper:
                seen_paper = True
                ans += sum(travel[0:i])
            if "M" in garbage[i] and not seen_metal:
                seen_metal = True
                ans += sum(travel[0:i])
            if seen_glass and seen_metal and seen_paper:
                break
        return ans

    def approach_1(self, garbage: List[str], travel: List[int]) -> int:
        """
        Can iterate from the back
        if seeing garbage type for the first time, start tracking
        time = travel + n_garbage
        """
        ans = 0
        seen_glass = False
        seen_metal = False
        seen_paper = False

        for i in range(len(garbage) - 1, -1, -1):
            for x in garbage[i]:
                match x:
                    case "G":
                        seen_glass = True
                    case "P":
                        seen_paper = True
                    case "M":
                        seen_metal = True
            ans += len(garbage[i])

            if i != 0:  # Will overflow to -1 if i == 0
                ans += travel[i - 1] if seen_glass else 0
                ans += travel[i - 1] if seen_metal else 0
                ans += travel[i - 1] if seen_paper else 0

        return ans


# @lc code=end
