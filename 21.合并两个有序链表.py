#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.mergeTwoLists(ListNode(1), ListNode(2))

# 我们可以如下递归地定义两个链表里的 merge 操作（忽略边界情况，比如空链表等）：

# list1[0]+merge(list1[1:],list2)
# list2[0]+merge(list1,list2[1:])

# 也就是说，两个链表头部值较小的一个节点与剩下元素的 merge 操作结果合并。
