#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.ret = True
        def dfs(node):
            if node and self.ret == True:
                if node.val != root.val:
                    self.ret =  False
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.ret
# @lc code=end

