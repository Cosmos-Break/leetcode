#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         def dfs(root, ans):
#             if root is None:
#                 return
#             if root.left:
#                 dfs(root.left, ans)
#             ans.append(root.val)
#             if root.right:
#                 dfs(root.right, ans)
#         ans = []
#         dfs(root, ans)
#         return ans
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            root = stack.pop()
            if isinstance(root, TreeNode):
                stack.extend([root.right, root.val, root.left])
            elif isinstance(root, int):
                ans.append(root)
        return ans

# @lc code=end

# 递归
# 迭代, 