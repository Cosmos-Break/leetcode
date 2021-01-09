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
        def isSym(root1, root2):
            if root1 == None and root2 == None:
                return True
            elif root1 != None and root2 != None:
                return root1.val == root2.val and isSym(root1.left, root2.right) and isSym(root1.right, root2.left)
            else:
                return False
        if root == None:
            return True
        else:
            return isSym(root.left, root.right)
            
# @lc code=end

