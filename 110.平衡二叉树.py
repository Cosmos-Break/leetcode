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
        def height(root: TreeNode):
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return - 1
            else:
                return 1 + max(left_height, right_height)
        return height(root) >= 0
# @lc code=end
# 自底向上的递归 类似于后序遍历  先看左右高度
# -1表示不平衡  如果有一个子树不平衡那么  整个肯定不平衡
# >=0 时代表高度