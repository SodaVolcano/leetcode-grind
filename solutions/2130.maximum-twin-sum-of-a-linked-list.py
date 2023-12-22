#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """Naive solution"""
        i = 0
        sums = []
        while head:
            sums.append(head.val)
            head = head.next

        n = len(sums)
        half = (n / 2) - 1
        for i in range(len(sums)):
            if i > half:
                break
            sums[n - 1 - i] += sums[i]
        return max(sums)


# @lc code=end
