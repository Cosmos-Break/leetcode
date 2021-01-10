#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = collections.deque([root])
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res[::-1]
# @lc code=end

# 宽搜, 使用deque, 判断出队节点的左右节点, 不空则入队
# 最后翻转操作使用[::-1]