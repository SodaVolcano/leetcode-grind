#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        go through each node
        if node.val != 0, sum += node.val
        else, make new ListNode and save it
        """
        linked_list = head.next
        current = linked_list.next

        while True:
            # Remove terminal node from linked list
            if current.val == 0 and current.next is None:
                linked_list.next = None
                break

            if current.val != 0:
                linked_list.val += current.val
                current = current.next
            else:
                linked_list.next = current.next
                linked_list = current.next
                current = current.next.next  # Have to be one node ahead

        return head.next


# @lc code=end
