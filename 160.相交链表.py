#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list_A = set()
        
        # step为10
        # while headA or headB:
        #     count = 0
        #     while headA:
        #         if headA in list_A:
        #             return headA
        #         else:
        #             list_A.add(headA)
        #             headA = headA.next
        #         count += 1
        #         if count == 10:
        #             break
            
        #     count = 0
        #     while headB:
        #         if headB in list_A:
        #             return headB
        #         else:
        #             list_A.add(headB)
        #             headB = headB.next
        #         count += 1
        #         if count == 10:
        #             break
        # return None

        while headA:
            if headA in list_A:
                return headA
            else:
                list_A.add(headA)
                headA = headA.next
        while headB:
            if headB in list_A:
                return headB
            else:
                list_A.add(headB)
                headB = headB.next
        return None
# @lc code=end

