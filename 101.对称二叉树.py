#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(left, right):
            if left is None and right is None:
                return True
            elif left is not None and right is not None:
                return left.val == right.val and isSym(left.left, right.right) and isSym(left.right, right.left)
            else:
                return False
        if root is None:
            return True
        else:
            return isSym(root.left, root.right)
                
            
# @lc code=end

# 和判断两棵二叉树相同相似. 因为这个就只有一棵树,所以要写个子函数.
# 不要忘记判断 节点的值 要相等.

