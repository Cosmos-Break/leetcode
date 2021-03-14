# @before-stub-for-debug-begin
from python3problem206 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
# @lc code=end

