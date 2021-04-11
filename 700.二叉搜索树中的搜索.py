#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        ret = None
        def dfs(node):
            nonlocal ret
            if node is None:
                return
            if node.val == val:
                ret = node
                return
            elif node.val < val:
                dfs(node.right)
            else:
                dfs(node.left)
        dfs(root)
        return ret
# @lc code=end

