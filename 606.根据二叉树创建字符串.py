#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""
        elif t.left is None and t.right is None:
            return str(t.val)
        elif t.right is None:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        else:
            return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
# @lc code=end

