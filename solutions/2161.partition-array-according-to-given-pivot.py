#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#


# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        - put elem less than pivot to LEFT
        - put elem bigger than pivot to RIGHT
        - put elem EQUAL to pivot next to pivot
        - maintain relative positioning

        naiive solution:
            left = [i for i in nums if i < pivot]
            right = [i for i in nums if i > pivot]
            middle = [i for i in nums if i == pivot]
            OR...
            for i in nums:
                if i > pivot, left.append(i)
                elif i < pivot, right.append(i)
                else middle.append(i)
            ans = left + middle + right
        """
        # Runtime beat 98.97% runtime... buddy what? probably just luck
        left = []
        right = []
        mid = []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                mid.append(i)
        return left + mid + right


# @lc code=end
