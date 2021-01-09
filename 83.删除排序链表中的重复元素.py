#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy_head = head
        while head is not None and head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy_head
# @lc code=end

