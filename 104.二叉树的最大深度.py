#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         else:
#             return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         queue = collections.deque([root])
#         level = 0
#         while queue:
#             size = len(queue)
#             for i in range(size):
#                 node = queue.popleft()
#                 if node is not None:
#                     queue.append(node.left)
#                     queue.append(node.right)
#             level += 1
#         return level - 1
import collections
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            level += 1
        return level
    
            
# @lc code=end
# 深搜(递归)
# 如果当前节点为空,则返回0
# 如果当前节点不为空,则返回1+ 左子树和右子树中较深的一个深度

# 宽搜(队列 deque)
# 最后要返回level-1, 
# 因为 如果当前只有一个root节点, 遍历完root节点之后 level=1
# 但此时deque里面还有两个空节点, 也要遍历 遍历完这一层之后 level=2
# 所以要返回level-1.

# 宽搜 优化成最后返回level 而不是level-1
# 检查出队节点的左节点和右节点, 当不为空时才入队.