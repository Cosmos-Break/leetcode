#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        inorder = []
        def dfs(node):
            nonlocal inorder
            if node is None:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        dfs(root)
        ret = float("inf")
        for i in range(1, len(inorder)):
            if inorder[i] - inorder[i-1] < ret:
                ret = inorder[i] - inorder[i-1]
        return ret
# @lc code=end

