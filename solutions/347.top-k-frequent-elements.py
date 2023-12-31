#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Okay, running this code multiple times gives 99.88% for runtime sometimes
        and 10% sometimes
        """
        from collections import Counter

        counts = Counter(nums)
        return [key for key, _ in counts.most_common(k)]

    def attempt_1(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        counts = Counter(nums)
        arr = sorted(counts.values(), reverse=True)[:k]
        return [key for (key, val) in counts.items() if val in arr]

    def attempt_1(self, nums: List[int], k: int) -> List[int]:
        """
        why the fuck is this slower than above????
        above:
            sort counts.values(), k iterations
            for key, val in counts.items() if val in arr - k iterations
            k * 2 iterations
        below:
            sort counts.keys(), k iterations
        the fuck?????
        """
        from collections import Counter

        counts = Counter(nums)
        return sorted(counts.keys(), key=lambda x: counts[x], reverse=True)[:k]


# @lc code=end
