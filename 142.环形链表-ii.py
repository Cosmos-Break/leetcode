#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            left = head.next
            right = head.next.next
            while left != right:
                left = left.next
                right = right.next.next
        except:
            return None
        right = head
        while left != right:
            left = left.next
            right = right.next
        return left

# @lc code=end

