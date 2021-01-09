#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def maxdepth(root):
            if root is None:
                return 0, True
            depth_left, isBal_left = maxdepth(root.left)
            depth_right, isBal_right = maxdepth(root.right)
            depth = 1 + max(depth_left, depth_right)
            isBal = abs(depth_left - depth_right) <= 1 and isBal_left and isBal_right
            return depth, isBal
        _, isBal=maxdepth(root)
        return isBal
# @lc code=end

