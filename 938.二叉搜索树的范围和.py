#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ret = 0
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.ret += node.val
                    dfs(node.left)
                    dfs(node.right)
                elif node.val < low:
                    dfs(node.right)
                elif node.val > high:
                    dfs(node.left)
        dfs(root)
        return self.ret
# @lc code=end
