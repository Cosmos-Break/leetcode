#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = float("inf")
        pre = -1
        def dfs(node):
            nonlocal ans, pre
            if node is None:
                return
            dfs(node.left)
            if pre == -1:
                pre = node.val
            else:
                ans = min(ans, node.val - pre)
                pre = node.val
            dfs(node.right)
        dfs(root)
        return ans
# @lc code=end

