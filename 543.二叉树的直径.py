#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_depth = 0
        def dfs(node):
            if node is None:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            ret_depth = max(left_depth, right_depth) + 1
            self.max_depth = max(self.max_depth, left_depth + right_depth)
            return ret_depth
        dfs(root)
        return self.max_depth

# @lc code=end

