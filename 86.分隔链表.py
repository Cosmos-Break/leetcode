#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head = ListNode(0)
        dummy_small_head = small_head
        big_head = ListNode(0)
        dummy_big_head = big_head
        while head is not None:
            if head.val < x:
                small_head.next = ListNode(head.val)
                small_head = small_head.next
            else:
                big_head.next = ListNode(head.val)
                big_head = big_head.next
            head = head.next
        small_head.next = dummy_big_head.next
        return dummy_small_head.next
# @lc code=end

