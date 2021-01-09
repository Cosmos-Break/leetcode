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
        current = head
        while current != None and current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
# @lc code=end
# current val和current next val值相等时, 把current指向跳过后面的节点
# 这时候不用再对current指针指向current.next 
# 因为还要比较current和current.next.next的值是否相等

