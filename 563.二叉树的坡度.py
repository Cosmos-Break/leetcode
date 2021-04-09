#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0
        def dfs(node):
            if node is None:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            self.tilt += abs(left_sum-right_sum)
            return left_sum + right_sum + node.val
        dfs(root)
        return self.tilt
# @lc code=end

