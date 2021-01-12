#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         def dfs(root, ans):
#             if root is None:
#                 return
#             ans.append(root.val)
#             dfs(root.left, ans)
#             dfs(root.right, ans)
#         ans = []
#         dfs(root, ans)
#         return ans

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ans = []
        while stack:
            root = stack.pop()
            if isinstance(root, TreeNode):
                stack.extend([root.right, root.left, root.val])
            elif isinstance(root, int):
                ans.append(root)
        return ans
# @lc code=end
# 递归
# 迭代