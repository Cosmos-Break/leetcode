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
        node_i = l1
        node_j = l2
        head = ListNode()
        dummy_node = head
        while node_i != None and node_j != None:
            new_node = ListNode()
            if node_i.val <= node_j.val:
                new_node.val = node_i.val
                node_i = node_i.next
            else:
                new_node.val = node_j.val
                node_j = node_j.next
            head.next = new_node
            head = new_node # 注意这边不是head = new_node.next 而是应该指向整个节点
            

        if node_i != None:
            left_node = node_i
        elif node_j != None:
            left_node = node_j
        else:
            left_node = None
        head.next = left_node
        return dummy_node.next
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.mergeTwoLists(ListNode(1), ListNode(2))