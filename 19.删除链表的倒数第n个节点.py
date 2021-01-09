#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = head
        for i in range(n):
            head = head.next
        left = dummy_head
        if head is None:
            return left.next
        while head.next is not None:
            head = head.next
            left = left.next
        left.next = left.next.next
        return dummy_head
# @lc code=end
# s = Solution()
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n1.next = n2
# n2.next = n3
# s.removeNthFromEnd(n1, 3)
