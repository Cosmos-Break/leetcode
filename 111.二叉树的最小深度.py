#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        min_dep = 10 ** 9
        if root.left:
            min_dep = min(self.minDepth(root.left), min_dep)
        if root.right:
            min_dep = min(self.minDepth(root.right), min_dep)
        return min_dep + 1
import collections
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         queue = collections.deque([root])
#         level = 1
#         while queue:
#             n = len(queue)
#             for i in range(n):
#                 node = queue.popleft()
#                 if node.left is None and node.right is None:
#                     return level
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             level += 1
#         return level

# @lc code=end

# 深搜
# 宽搜