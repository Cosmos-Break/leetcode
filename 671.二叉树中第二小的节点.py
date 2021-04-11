# @before-stub-for-debug-begin
from python3problem671 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min_1 = min_2 = float("inf")
        def dfs(node):
            nonlocal min_1, min_2
            if node is None:
                return
            if node.val < min_1:
                min_2 = min_1
                min_1 = node.val
            elif node.val < min_2 and node.val != min_1:
                min_2 = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return min_2 if min_2 != float("inf") else -1
# @lc code=end

