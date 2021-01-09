#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        counter = 0
        dummy_head = head
        while head:
            counter += 1
            head = head.next
        head = dummy_head
        k = k % counter
        if k == 0:
            return head
        for i in range(k):
            head = head.next
            if head is None:
                head = dummy_head
        left = dummy_head
        while head.next is not None:
            head = head.next
            left = left.next
        new_head = left.next
        left.next = None
        head.next = dummy_head
        return new_head
        
# @lc code=end
s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
s.rotateRight(n1, 1)
