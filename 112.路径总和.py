#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# import collections
# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if root is None:
#             return False
#         queue = collections.deque([root])
#         queue_val = collections.deque([root.val])
#         while queue:
#             root = queue.popleft()
#             val = queue_val.popleft()
#             if not root.left and not root.right and val == sum:
#                 return True
#             if root.left:
#                 queue.append(root.left)
#                 queue_val.append(val + root.left.val)
#             if root.right:
#                 queue.append(root.right)
#                 queue_val.append(val + root.right.val)
#         return False

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        
# @lc code=end
# if root.left is None and root.right is None 确保当前节点为叶子节点 很重要
# 宽搜 一个一个遍历队列里的节点,而不是一行一行的遍历
# 深搜 递归, 如果不是叶子节点, 判断 sum-root.val 是否等于左子树 或 右子树
